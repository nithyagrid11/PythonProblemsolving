from datetime import datetime

class Node:
    def __init__(self,task_id,description,current_status,due_date):
        self.task_id = task_id
        self.description = description
        self.current_status = current_status
        self.due_date = due_date
        self.next = None

class Todolist:
    def __init__(self):
        self.start = None
        self.current_id = 1
    def gen_id(self):
        task_id = self.current_id
        self.current_id += 1
        return task_id
    def create(self,desc,current_status,due_date_str):
        due_date = datetime.strptime(due_date_str,"%d-%m-%Y")
        task_id = self.gen_id()
        new_node = Node(task_id,desc,current_status,due_date)
        if self.start is None:
            self.start = new_node
        else:
            p = self.start
            while p.next is not None:
                p = p.next
            p.next = new_node
    def read_all(self):
        if self.start is None:
            print('List is empty')
            return
        p = self.start
        while p is not None:
            print(f"Id: {p.task_id} | Description: {p.description} | Current_status: {p.current_status} | Due_date: {p.due_date.strftime('%d-%m-%Y')}")
            print()
            p = p.next
        return
    def update(self):
        if self.start is None:
            print('List is empty')
            return
        self.read_all()
        enter_id = int(input("Enter the id of the task you want to make changes: "))
        print()
        p = self.start
        while p is not None:
            if p.task_id == enter_id:
                print()
                print(f"description: {p.description} | current_status: {p.current_status} | due_date: {p.due_date.strftime('%d-%m-%Y')}")
                print()
                print("Choose one option to update a field: ")
                while True:
                    print("1.Description")
                    print("2.Status")
                    print("3.Due Date")
                    print("4.Exit")
                    option_update = input("Choose one option from above: ")
                    if option_update == '1':
                        new_desc = input("Enter a new description: ")
                        p.description = new_desc
                    elif option_update == '2':
                        p.current_status = not p.current_status
                        print('Status is toggled')
                    elif option_update == '3':
                        new_due_date = input("Enter a new due date: ")
                        p.due_date = datetime.strptime(new_due_date,"%d-%m-%Y")
                    elif option_update == '4':
                        print('Task updated')
                        return
                    else:
                        print("Invalid option entered.")
            p = p.next
        print('Task not found')
    
    def delete(self):
        if self.start is None:
            print('List is empty')
            return
        self.read_all()
        enter_id = int(input("Enter the id to perform deletion option: "))
        prev = None
        p = self.start
        
        while p is not None:
            if p.task_id == enter_id:
                if prev is None: #deleting head
                    self.start = p.next
                else:
                    prev.next = p.next #handles deletion in b/w and at end
                print('Task deleted')
                return 
            prev = p
            p = p.next
        print('Task not found')

t1 = Todolist()

print("Available option:")
#menu
while True:
    print("1. Create a task")
    print("2. Read/Fetch all tasks")
    print("3. Update the task")
    print("4. Delete a task")
    print("5. Exit")

    option = input("Enter one option: ")
    if option == '1':
        description = input("Enter description: ")
        current_status = False
        due_date = input("Enter the due date (dd-mm-yyyy): ")
        t1.create(description,current_status,due_date)
    elif option == '2':
        t1.read_all()
    elif option == '3':
        t1.update()
    elif option == '4':
        t1.delete()
    elif option == '5':
        exit()
    else:
        print('Invalid option')