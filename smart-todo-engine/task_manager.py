from dataclasses import dataclass, field
from task import Task,Priprity
from typing import Optional,Iterator
import time
from math import inf

from enum import Enum

class SortItem(Enum):
        deadline = "deadline"
        priority = "Priority"
        old_to_new = 'old_to_new'
        new_to_old = 'new_to_old'
        
        
@dataclass(slots=True)
class Manager:
    _tasks:dict = field(default_factory=dict) 
    _compalated_tasks:dict = field(default_factory=dict) 
    # _pending_tasks:list[Task] = field(default_factory=dict)

    def add_task(self,**task_item)->Task:
        if  not task_item['title']:
            raise  ValueError('title of task must be annonation')
        match priority:=task_item['priority']:
            case '1' | Priprity.low :
                priority= Priprity.low
            case '2' |  Priprity.medium  :
                priority= Priprity.medium
            case '3' |  Priprity.high  :
                priority= Priprity.high
            case _ :
                priority = Priprity.low
            
        if not task_item['tags'] == None and not isinstance(task_item['tags'],tuple) :
            task_item['tags'] = tuple(task_item['tags'])
        
        if task_item['status'] is True:
            task_item['completed_at'] = time.monotonic()
        
        if task_item['deadline']:
            task_item['deadline'] = time.monotonic() * (60 * int(task_item['deadline']))
        
        task = Task(**task_item)
        self._tasks[task_item['title']] = task
        return task
    
    def remove_task(self, title:str)->None:
        if title in self._tasks:
            del self._tasks[title]
        else:
            print(f'{title} not found')

    def updata_task(self,title:str, task_dict:dict)->Optional[Task]:
        if self.validation(title, f'{title} not found'):
            task =self._tasks
            data = task[title].__dict__ | task_dict
            newTask = Task(**data)
            task[title] = newTask
            del task[title]
            task[newTask.title] = newTask
            # for key, value in self._tasks.items():
            #     if key != value.title:
            #         self._tasks[value.title] = newTask
            return newTask


    def search_task(self, title:str)->Task:
        if self.validation(title, f'{title} not found'):
            return self._tasks[title]
        
    def toggle_complate(self,title:str)->None:
        if self.validation(title, f'{title} not found'):
            status = self._tasks[title].status
            status = not status 
            if status:
                self._tasks[title].completed_at = time.monotonic()
                self._compalated_tasks[title] = self._tasks[title]
            else:
                del self._compalated_tasks[title]
    def __iter__(self)->Iterator[Task]:
        return iter(self._tasks.values())
    
    def all_tasks(self):
        
        data = self._tasks.keys()
        return tuple(data)
       
    
    def validation(self,title:str,print_value:str):
        print(self._tasks.keys())
        if title in self._tasks:
            return True
        else:
            print(print_value)
            return  False
    def sort(self,key:SortItem):
        tasks = self._tasks.values()
        match key:
            case SortItem.priority:
              sorted_by_priority =  sorted(tasks,key=lambda x: x.priority,reverse=True)
              return tuple([task.title for task in sorted_by_priority])
        
            case SortItem.deadline:
                sorted_by_deadline =  sorted(tasks,key=lambda x: x.deadline)
                return tuple([task.title for task in sorted_by_deadline])
            case SortItem.old_to_new:
                sorted_by_create_at =  sorted(tasks,key=lambda x: x.created_at,reverse=True)
                return tuple([task.title for task in sorted_by_create_at])
            case SortItem.new_to_old:
                new_to_old = reversed(self.sort(SortItem.old_to_new))
                return tuple(new_to_old)
# data_1 = {
#     'title':'matin',
#     'priority':1,
#     'tags':('python',)

# }
# data_2 = {
#     'title':'read a book',
#     'priority': 3,
#     'created_at':time.monotonic(),
#     'tags':['python','programming'],
#     'deadline':time.monotonic() + (60**2),
#     'status':True
# }


