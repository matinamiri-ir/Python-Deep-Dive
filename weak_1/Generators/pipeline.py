from typing import  Callable, Iterator
from functools import reduce

class Pipeline:
    def __init__(self,data:Iterator):
        self._data:Iterator = data
        
    def __iter__(self):
        return iter(self._data)
    
    def map(self,func:Callable):
        self._data = map(func, self._data)
        return self
    
    def filter(self, func:Callable):
        self._data = filter(func, self._data)
        return self

    def reduce(self):
        return reduce(lambda a,b : a+b, self._data)
     
    def __str__(self):
        return f'<{self.__class__.__name__} Type>'
    
    def __repr__(self):
        return f'{self.__class__.__name__} type x{id(self)}'  
        
t  = Pipeline([1,2,3])

print(t.map(lambda x: x**2).filter())
repr(t)
