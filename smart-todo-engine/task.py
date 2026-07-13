from dataclasses import dataclass, field
from time import monotonic
from enum import IntEnum
from math import inf
class Priprity(IntEnum):
    high = 3
    medium = 2
    low = 1

@dataclass
class Task:
    title:str
    description:str = ''
    priority:Priprity = Priprity.low
    status:bool = False
    created_at:float = field(default_factory=monotonic)
    deadline:float = field(default=inf)
    tags:tuple[str,...]  = field(default_factory=tuple)
    completed_at:float | None = None
    def __str__(self):
        return f"<task's title = {self.title!r}, pripority = {self.priority}  task`s status = {'done' if self.status else 'undone'!r}>"
    
    def __repr__(self):
        return f'<{self.title=!r}, {self.priority=}, {self.status=!r}>'
    
    def __eq__(self, other):
        if isinstance(other,self.__class__):
            return self.title == other.title
        else:
            return NotImplemented
        
        
