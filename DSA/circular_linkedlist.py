class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class CLL:
    def __init__(self):
        self.last = None
    def display(self):
        if self.last is None:
            print('List is empty')
            return
        p = self.last.next
        while True:
            print(p.value," ",end = ' ')
            p = p.next
            if p == self.last.next:
                break
        print()
    def insert_at_beginning(self,value):
        temp = Node(value)
        if self.last is None:
            self.last = temp
            temp.next = temp
            return
        temp.next = self.last.next
        self.last.next = temp
    def insert_at_end(self,value):
        temp = Node(value)
        if self.last is None:
            self.last = temp
            temp.next = temp
            return
        temp.next = self.last.next
        self.last.next = temp
        self.last = temp
        print()
    def insert_after(self,x,value):
        if self.last is None:
            print('List is empty')
            return
        p = self.last.next
        while True:
            if p.value == x:
               temp = Node(value)
               temp.next = p.next
               p.next = temp
               if p == self.last: #if x is at self.last then we are adding after the self.last so we need to update the self.last
                self.last = temp
                return
            p = p.next
            if p == self.last.next:
                break
        print()
    def insert_before(self,x,value):
        if self.last is None:
            print('List is empty')
            return
        curr = self.last.next
        prev = self.last
        while True:
            if curr.value == x:
                temp = Node(value)

                temp.next = curr
                prev.next = temp
                #if curr == self.last.next:
                    #self.last.next = temp
                #return
            prev = curr
            curr = curr.next
            if curr == self.last.next:
                break
        print('Value not found')
    def delete(self,x):
        if self.last is None:
            print('List is empty')
            return
        curr = self.last.next
        prev = self.last

        if curr == self.last and curr.value == x:#only node
            self.last = None
            return
        while True:
            if curr.value == x:
                prev.next = curr.next
                if curr == self.last:
                    self.last = prev
                return
            prev = curr
            curr = curr.next
            if curr == self.last.next:
                break
        print('Value not found')
        
c1 = CLL()
while True:
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Display")
    print("4. Insert after a specific node")
    print("5. Insert before a specific node")
    print("6. Delete a node")
    print('7. Exit')
    option = input("Enter an option: ")
    if option == '1':
        value = int(input('Enter a value: '))
        print(c1.insert_at_beginning(value))
    elif option == '2':
        value = int(input('Enter a value: '))
        print(c1.insert_at_end(value))
    elif option == '3':
        c1.display()
    elif option == '4':
        value = int(input('Enter the value to be inserted: '))
        x = int(input('Enter the element after which to insert: '))
        c1.insert_after(x,value)
    elif option == '5':
        value = int(input('Enter the value to be inserted: '))
        x = int(input('Enter the element before which to insert: '))
        c1.insert_before(x,value)
    elif option == '6':
        x = int(input('Enter the value to delete'))
        c1.delete(x)
    elif option == '7':
        exit()
    else:
        print('Invalid option')