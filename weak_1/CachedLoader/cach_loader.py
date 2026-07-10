import time
from collections import OrderedDict
from typing import Any, Callable
from threading import Lock,Event
from concurrent.futures import ThreadPoolExecutor
from cach import Cach
from exception import FunctionValueError

class CahchLoader:
    
    def __init__(self,func:Callable,ttl:float=10,lru_item:int=100):
        self._data:OrderedDict[str,Cach] = OrderedDict()
        self._function = func
        self.__worker = OrderedDict()
        self.__lock:Lock = Lock()
        self.__events:dict[str,Event] = {}
        self._ttl:float = ttl
        self._lru_item = lru_item
        
    def load(self,api:str):
        #prepare
        with self.__lock:
            if api not in self.__events:
                self.__events[api] = Event()
            
        #state_1
        with self.__lock:
            if api in self._data:
                if not self._data[api].is_expire():
                    print('block_1')
                    self._data.move_to_end(api)
                    return self._data[api]
         
        #state_2
        with self.__lock:
            if api in self.__worker:
                event = self.__events[api]
                is_worker = False
            else:
                event = None
                self.__worker[api] = True
                is_worker = True
                
        if not is_worker:
            event.wait()
            return self._data[api]    
                
        
        #state_3
    
        try:
            print('block_3')
            result = self.__work(api)
            cach = Cach(api,result, TTL=0.01, created_at=time.monotonic())
            with self.__lock:
                self.__add_data_to_cach(api,cach)
                res = self._data[api]   
        
            self.__events[api].set()   
            return res
        finally:
            with self.__lock:
                self.__events[api].set()
                del self.__worker[api]
                del self.__events[api]
               
               

                
                    
                
                
    
    def __work(self, api:str)->Any:
        try: 
            data = self._function(api)
            return data
        except Exception :
            raise FunctionValueError(f'can not fetch data from {self._function.__name__}')
           
    def __add_data_to_cach(self,api:str,data:Any):
        if len(self._data) >= self._lru_item :
            self._data.popitem(last=False)
            self._data[api] = data
        else:
            self._data[api] = data
            
            

def fetch(api:str)->str:
    time.sleep(0.1)
    return f'user fetched --> {api}'



cach = CahchLoader(fetch)


def test():
    
    print(cach.load('matin'))
    print('*'*100)
        
def main():
    with ThreadPoolExecutor(max_workers=100) as executer:
        for _ in range(1000):
            executer.submit(test)
        
# if __name__ == "__main__":
main()