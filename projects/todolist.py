from datetime import datetime

class Todolist:
    def __init__(self):
        self.current_id = 1
        self.list_items = []

    def gen_id(self):
        task_id = self.current_id
        self.current_id += 1
        return task_id
    
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
        print()
    #fetching specific fields of a particular id
    def read_by_id(self,task_id,field=None):
        for task in self.list_items:
            if task['id'] == task_id:
                if field:
                    return task.get(field)
                return task
        return None

    #updating all 3 fields
    def update(self):
        self.read_all()
        task_id = int(input('Choose the id to perform update action: '))
        for task in self.list_items:
            if task['id'] == task_id:
                print("Description: ", task['description'])
                print("Current_status: ", task['current_status'])
                print("Due-Date: ", task['due_date'].strftime('%d-%m-%Y'))
                
                print('Choose one option to which you would like to update/modify')
                while True:
                    print('1.Description')
                    print('2.Current Status')
                    print('3.Due date')
                    print('4.Exit')
                    option = input("Enter one option: ")
                    if option == '1':
                        new_desc = input("Enter a new description to update old one")
                        task['description'] = new_desc
                    elif option == '2':
                        task['current_status'] = not task['current_status']
                        print("Status is toggled")
                    elif option == '3':
                        new_due_date = input('Enter a new date (dd-mm-yyyy): ')
                        task['due_date'] = datetime.strptime(new_due_date,"%d-%m-%Y")
                    elif option == '4':
                        return 'Task updated'
                    else:
                        print('Invalid option')
        return 'Task not found'
        
    
    #delete a task
    def delete(self):
        self.read_all()
        task_id = int(input("Enter the id you want to delete: "))
        for task in self.list_items:
            if task['id'] == task_id:
                print('Task found')
                choose = input('Are you sure you want to delete (y/n)?')
                if choose.lower() == 'y':
                    self.list_items.remove(task)
                    return 'Task deleted'
                else:
                    return "Deletion cancelled"
        return 'Task not found'

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
        t1.read_all()
    elif option == '3':
        task_id = int(input('Enter the task id of a task you want to read: '))
        field = input('Enter the field (description,current_status,due_date) you want to read: ')
        result = t1.read_by_id(task_id,field)
        print(result)
    elif option == '4':
        t1.update()
    elif option == '5':
        print(t1.delete())
    elif option == '6':
        break
    else:
        print('Invalid choice')