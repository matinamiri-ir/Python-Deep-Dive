from typing import Union, Any
import json
from types import MappingProxyType

class Config:
    def __init__(self,path:str):
        object.__setattr__(self,'_path', path)
        object.__setattr__(self,'_data', Config.load(self._path))  
        object.__setattr__(self,'_item',Item(self._data))
    def __getattr__(self, name:str)->Any:
        data = getattr(self._item,name) 
        return data
    
    def __setattr__(self, name, value):
            raise AttributeError('can not set new value')

    
    def __delattr__(self, name):
        raise AttributeError('can not delete Attribute from Config.json')
    
    def __contains__(self, item):
        return item in self._data.keys()
    
    def __hash__(self):
        return hash(tuple(self._data.items()))
    
    def __eq__(self, other):
        if isinstance(other,Config):
            return self._data.items() == other._data.items()
        else:
            return NotImplemented
    
    def __iter__(self):
         return iter(self._data.keys())  
      
    def __str__(self):
        return f'<Config {self._path}>'
    
    def __repr__(self):
        return f'<{self.__class__.__name__} path:{self._path} len:{len(self._data)}>'
    
    def __len__(self):
        return len(self._data.keys())
        
    @staticmethod
    def load(file_name:str)->Union[dict,list]:
        with open(file_name, 'r' , encoding='utf-8') as file:
           data = json.load(file)
           return data
       
class Item:
    def __init__(self, data:dict | list):
        if isinstance(data, dict):
            data = MappingProxyType(data)
            object.__setattr__(self,'_data',data)
        elif isinstance(data,tuple):
            object.__setattr__(self,'_data',data)

    def __str__(self):
        return str(self._data)
    
    def __repr__(self):
        return f'<{self.__class__.__name__} data = {self._data}>'
    
    def __getattr__(self, name:str)->Any:
        if name.startswith('_') and name.endswith('_'):
            name = name[1:-1]
        try:
            data = self._data[name]
            if isinstance(data,dict):
                return Item(data)
            elif isinstance(data,list):
                return Item(tuple(data))
            else:
                return data
        except KeyError :
            raise AttributeError(f"{name!r} not found")
         
    def __setattr__(self, name, value):
        raise AttributeError('can not set new value')  
    
    def __iter__(self):
        return iter(self._data.keys())
      
    def __getitem__(self, key):
        data =self._data[key]
        match data:
            case dict():
                return Item(data)
            case list():
                return Item(tuple(data))
            case _:
                return data


js = Config('config.json')


