class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.start = None
    def display_list(self):
        if self.start is None:
            print('List is empty')
            return 
        else:
            print('List: ')
            p = self.start
            while p.next is not None:#printing till the 2nd last node
                print(p.value,end='->')
                p = p.next
            print(p.value) #printing last value
    def insert_at_the_beginning(self,data):
        temp = Node(data)
        temp.next = self.start
        self.start = temp
    def insert_at_end(self,data):
        temp = Node(data)
        if self.start is None: #empty linkedlist
            self.start = temp
            return
        p = self.start #linkedlist is there 
        while p.next is not None:
            p = p.next
        p.next = temp #adding temp at the end
    def create_list(self):
        n = int(input("Enter number of nodes: "))
        if n == 0:
            return 'no nodes'
        for i in range(n):
            data = int(input('Enter the value: '))
            self.insert_at_end(data)
    def insert_after(self,x,new_node):
        p = self.start
        while p is not None:
            if p.value == x:
                temp = Node(new_node)
                temp.next = p.next
                p.next = temp
                return
            p = p.next
        print('Element not found')


#menu
list1 = SingleLinkedList()
list1.create_list()
print('Options: ')

while True:
    print('1: Display list')
    #print('2: Count the number of nodes')
    #print('3: search for an element')
    print('4: Insert at the beginning')
    print('5: Insert at the end')
    print('6: Insert after a specific node')
    print('7:Exit')


    choice = int(input('Choose one option: '))
    if choice == 1:
        list1.display_list()
    elif choice == 4:
        data = int(input('Enter the element to be inserted: '))
        list1.insert_at_the_beginning(data)
    elif choice == 5:
        data = int(input('Enter the element to be inserted at the end: '))
        list1.insert_at_end(data)
    elif choice == 6:
        x = int(input('Enter the element after which to insert: '))
        new_node = int(input('Enter the new node to be inserted: '))
        list1.insert_after(x,new_node)
    elif choice == 7:
        break
    else:
        print('Wrong option')
    print()