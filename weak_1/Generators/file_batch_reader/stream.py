from pathlib import Path
from typing import Iterable, Generator, Iterator
class FileBatchReader:
    def __init__(self,
                 paths:Iterable[Path],
                 batch_size:int=4,
                 encoding:str ='utf-8',
                 skip_empty :bool =True):
        
        if paths:=tuple(paths):
            self._paths = paths
        else:
            raise ValueError('please pass at least one path')
        if batch_size <= 0 :
            raise ValueError('batch size must be positive')
        self._batch_size = batch_size
        self.encoding = encoding
        self._skip_empty = skip_empty
        
    def __iter__(self)->Iterator[list[str]]:
        return self._iter_batch()
        
    
    def __enter__(self)->"FileBatchReader":
        return self
    
    def __exit__(self, exc_type, exc, tb)->None:
        return 
    
    def _iter_batch(self)->Iterator[list[str]]:
        iters = self._paths_iter()
        
        while True:
            group = []
            for _ in range(self._batch_size):
                try:
                    group.append(next(iters))
                except StopIteration :
                    break
            if not group:
                break
            yield group
            
    def _paths_iter(self)->Iterator[str]:
        for path in self._paths:
            yield from self._file_get(path)
            
                
    def _file_get(self,path:Path)->Generator[str]:
        try:
            with path.open('r', encoding=self.encoding) as file:
                for line in file:
                    if self._skip_empty:
                        if line.strip():
                            yield line.strip()
                        else:
                            continue   
                    else:
                        yield line
                        
        except FileNotFoundError:
            raise FileNotFoundError('file not found')
                    
        
                    
paths= (Path(path) for path in ['a.txt','b.txt','admins.txt'] )
p = FileBatchReader(paths,batch_size=3)

for admin in p:
    print(admin)
print('--'*20)
for admin in p:
    print(admin)
    
