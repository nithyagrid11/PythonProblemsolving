class Node:
    def __init__(self,value):
        self.prev = None
        self.next = None
        self.value = value
class Double_Linkedlist:
    def __init__(self):
        self.start = None
    def display(self):
        if self.start is None:
            print('List is empty')
            return
        p = self.start
        while p is not None:
            print(p.value, " ",end = " ")
            p = p.next
        print()
    def insert_at_beginning(self,value):
        temp = Node(value)
        if self.start is None:
            self.start = temp
            return
        temp.next = self.start
        self.start.prev = temp
        self.start = temp
    def insert_at_end(self,value):
        temp = Node(value)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p
    def insert_after_node(self,x,value):
        temp = Node(value)
        p = self.start
        while p is not None:
            if x == p.value:
                temp.prev = p
                temp.next = p.next
                if p.next is not None:
                    p.next.prev = temp
                p.next = temp
                break
            p = p.next
        print()
    def insert_before_node(self,x,value):
        if self.start is None:
            print('List is empty')
            return
        p = self.start
        while p is not None:
            if p.value == x:
                if p.value == x and p.prev is None: #inserting before head case
                    self.insert_at_beginning(value)
                    return
                temp = Node(value)
                temp.prev = p.prev
                temp.next = p
                
                p.prev.next = temp
                p.prev = temp
                return
            p = p.next
        print()
    def delete_node(self,x):
        if self.start is None:
            print('List is empty')
            return
        p = self.start
        while p is not None:
            if p.value == x:
                #deleting head
                if p.prev is None:
                    self.start = p.next
                    if self.start is not None:
                        self.start.prev = None
                    return
                #deleting middle or last
                p.prev.next = p.next
                if p.next is not None:
                    p.next.prev = p.prev
                return
            p = p.next
        print('Value not found')
    def reverse_dll(self):
        if self.start is None:
            print('List is empty')
            return
        '''p1 = self.start
        p2 = p1.next
        p1.next = None
        p1.prev = p2
        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev
        self.start = p1'''
        p = self.start
        temp = None
        while p is not None:
            # Swap next and prev
            temp = p.prev
            p.prev = p.next
            p.next = temp
            # Move to next node (which is previous before swap)
            p = p.prev
        # Fix start
        if temp is not None:
            self.start = temp.prev
        
d1 = Double_Linkedlist()
while True: 
    print("1. Display List")
    print("2. Insert a node at beginning")
    print("3. Insert a node at end")
    print("4. Insert a node after a specific node")
    print("5. Insert a node before a specific node")
    print("6. Delete a node")
    print("7. Reverse the dll")
    print("8. Exit")

    option = input('Enter an option: ')
    if option == '1':
        d1.display()
    elif option == '2':
        value = int(input('Enter a value: '))
        d1.insert_at_beginning(value)
    elif option == '3':
        value = int(input('Enter a value: '))
        d1.insert_at_end(value)
    elif option == '4':
        value = int(input('Enter the element to be inserted: '))
        x = int(input("Enter the element after which to insert: "))
        d1.insert_after_node(x,value)
    elif option == '5':
        value = int(input('Enter the element to be inserted: '))
        x = int(input("Enter the element before which to insert: "))
        d1.insert_before_node(x,value)
    elif option == '6':
        x = int(input('Enter the element to be deleted: '))
        d1.delete_node(x)
    elif option == '7':
        d1.reverse_dll()
    elif option == '8':
        exit()
    else:
        print("Invalid option")
