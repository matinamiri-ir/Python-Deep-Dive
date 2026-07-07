from abc import ABC, abstractmethod
from typing import Callable
class Validation(ABC):
    def __set_name__(self,owner,name):
        self._name = name
        
    @abstractmethod
    def __set__(self, instance, value):
        pass
        
    @abstractmethod
    def __get__(self, instance, owner):
        pass
    
    
class Number(Validation):
    def __init__(self,
                 type:type,
                 min:int=None,
                 max:int = None,
                 immute:bool=True,
                 custom_validate:Callable=None,
                 default:int | float=None ):
        self.min = min
        self.max = max
        self.immute = immute
        self.custom_validation = custom_validate
        self.default =default 
        self.__type = type
        
    def __set__(self, instance, value):
        try:
            value = self.__type(value)
        except ValueError :
            raise ValueError(f'{value} must be {self.__type} or list')
        if  isinstance(value,self.__type):
            self._validate_type(instance,value)
        
        elif isinstance(value,list):
            exc_type = self.__type
            for number in value:
                self._validate_type(instance,exc_type(number))
        
            
        instance.__dict__[self._name] = value   

    def _validate_type(self,instance,value)->None:
        if isinstance(value,self.__type):
            if self.custom_validation:
                if not self.custom_validation(value):
                    raise ValueError('value is not acceptable')
            else:
                if  self.min is not None:
                    if self.min > value:
                            raise ValueError(f'{value} must greater than {self.min}')
                if self.max is not None:
                    if value > self.max:
                            raise ValueError(f'{value} must lesser than {self.max}')
                        
                if self.immute and self._name in instance.__dict__:
                    raise TypeError(f'{self.__class__.__name__} is Immutable Type')
        else:
            raise ValueError(f'{value} must be {self.__type}')
            
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self._name,self.default)
        
class Integer(Number):
    def __init__(self , min = None, max = None, immute = False, custom_validate = None, default = None):
        super().__init__(int, min, max, immute, custom_validate, default)

    
class Float(Number):
    def __init__(self,  min = None, max = None, immute = False, custom_validate = None,default:float = None):
        super().__init__(float, min, max, immute, custom_validate,float(default) if default is not None else None)
        


class String(Validation):
    def __init__(self,string:str=None,min_lenght:int = 0 , max_length:int = None):
       #self._string = str(string) if string else None
        self._min_length = min_lenght
        self._max_length = max_length
    
    def __set__(self, instance, value:str):
        value = str(value)
        if len(value) < self._min_length:
            raise ValueError(f'len {value} must be greater than {self._min_length}')
        elif self._max_length is not None and len(value) > self._max_length:
            raise ValueError(f'the length of {value} must be less then {self._max_length}')
        else:
            instance.__dict__[self._name] = value
            
    def __get__(self, instance, owner):
        if instance:
            return instance.__dict__[self._name]
        else:
            return self
        
