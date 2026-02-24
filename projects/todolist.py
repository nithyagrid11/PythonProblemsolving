from datetime import datetime

class Todolist:
    def __init__(self):
        self.current_id = 1
        self.list_items = []

    def gen_id(self):
        id = self.current_id
        self.current_id += 1
        return id
    
    def create(self,desc,current_status,due_date_str):

        ''' desc = string input
        current_status = boolean value
        due_date = datetime object'''
        due_date = datetime.strptime(due_date_str,"%d-%m-%Y")

        task_details = {
            'id' : self.gen_id(),
            'description' : desc,
            'current_status': current_status,
            'due_date': due_date
        }
        self.list_items.append(task_details)

    def read_all(self):
        for task in self.list_items:
            print(
            f"ID: {task['id']}, "
            f"Description: {task['description']}, "
            f"Status: {task['current_status']}, "
            f"Due Date: {task['due_date'].strftime('%d-%m-%Y')}"
            )

    #fetching specific fields of a particular id
    def read_by_id(self,task_id,field=None):
        for task in self.list_items:
            if task['id'] == task_id:
                if field:
                    return task.get(field)
                return task
        return None
    
    #updating status and due_date
    def update(self,task_id):
        for task in self.list_items:
            if task['id'] == task_id:
                task['current_status'] = not task['current_status']
                new_due_date = int(input('Enter a new date: '))
                task['due_date'] = datetime.strftime(new_due_date,"%d-%m-%Y")
                return True
        return False
    
    #delete a task
    def delete(self,task_id):
        for task in self.list_items:
            if task['id'] == task_id:
                if task['current_status'] == True:
                    self.list_items.remove(task)
                    return 'Task completed'
                else:
                    return "Task is not completed, can't delete"
        return 'Task not found'


#practise
t1 = Todolist()

while True:
    print('Options')
    print('1 -> Create/Add a task')
    print('2 -> Read/Fetch all tasks')
    print('3 -> Read/Fetch a specific task')
    print('4 -> Update a task')
    print('5 -> Delete a task')
    print('6 -> Exit')

    option = input('Enter one option: ')

    if option == '1':
        desc = input('Enter task description: ')
        status = False
        due_date = input('Enter a due date (dd-mm-yyyy): ')
        t1.create(desc,status,due_date)
    elif option == '2':
        print(t1.read_all())
    elif option == '3':
        task_id = int(input('Enter the task id of a task you want to read: '))
        field = input('Enter the field (description,current_status,due_date) you want to read: ')
        result = t1.read_by_id(task_id,field)
        print(result)
    elif option == '4':
        task_id = int(input('Enter the task id you want to make changes: '))
        t1.update(task_id)
    elif option == '5':
        task_id = int(input('Enter the task to check status and delete: '))
        print(t1.delete(task_id))
    elif option == '6':
        break
    else:
        print('Invalid choice')