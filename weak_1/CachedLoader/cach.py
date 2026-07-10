from dataclasses import dataclass,field
import time
from typing import Any
@dataclass
class Cach:
    key:str
    value:Any
    TTL:float
    created_at : float = field(default_factory=time.monotonic)
    
    def is_expire(self)->bool:
        return time.monotonic() >= self.created_at + (self.TTL )