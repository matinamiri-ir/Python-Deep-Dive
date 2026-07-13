from task_manager import Manager

def main():
    manager = Manager()
    while True:
        print('*'*100)
        print('welcome to Task manager  ')
        chose = int(input('please enter your plan:\n\t1)Add Task\n\t2)All Tasks\n\t3)Complated Task\n\t4)remove Task\n\t5)Updata Task\n\t6)Change Task State\n\t7)Exit\n'))
        match chose:
            case 1:
                print('Add New Task')
                items = ['title','description','priority','status','deadline','tags']
                taks_item = dict()
                for i in items:
                    if i =='priority':
                        taks_item[i] = input(f'Please Enter {i.title()} (1-3) default = 1\n')
                    elif i == 'tags':
                        taks_item[i] = input(f'Please Enter Your {i.title()} sprate with space\n').split()
                    elif i == 'deadline':
                        taks_item[i] = input('Please Enter Your Deadline mins or skip with Enter\n')
                    elif i == 'status':
                        ansewr = input('if task is done enter 1 eles skip with Key\n'.title())
                        taks_item[i] = True if ansewr == '1' else False
                    else:
                        taks_item[i] = input(f'please enter the {i} of Task\n'.title())
                manager.add_task(**taks_item)
                print(f"{taks_item['title']} created successfuly")
            case 2:
                
                tasks = manager.all_tasks()
                if tasks:
                    star = len(str(tasks))
                    print('*'*star)
                    for task in tasks:
                        print(task)
                    print('*'*star)
                else:
                    print('tasks not found'.title())
            case 3 :
                ...
            case 4:
                task_name = input('please enter what task you want to delete\n'.title())
                try:
                    manager.remove_task(task_name)
                except:
                    print('task not removed'.title())
                else:
                    print('task removed successfuly'.title())
            case 6:
                task_name = input('please enter what task you want to change status/n'.title())
                try:
                    manager.toggle_complate(task_name)
                except:
                    print('sorry we have some problem for change status')
                else:
                    print(f"the {task_name}'s status was change successfuly")
            case 7:
                break
    
if __name__ == '__main__':
    main()