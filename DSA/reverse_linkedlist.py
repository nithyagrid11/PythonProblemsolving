class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.start = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = new_node
    def create_list(self):
        n = int(input("Enter number of nodes: "))
        for i in range(n):
            value = int(input("Enter value: "))
            self.insert_at_end(value)
        print("List is created")
    def display(self):
        if self.start is None:
            print("List is empty")
            return
        p = self.start
        while p is not None:
            print(p.value, end=" ")
            p = p.next
        print()
    def reverse_list(self):
        prev = None
        curr = self.start
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.start = prev

l1 = LinkedList()

while True:
    print("\nOptions:")
    print("1. Create list")
    print("2. Insert at end")
    print("3. Display")
    print("4. Reverse")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        l1.create_list()
    elif choice == '2':
        value = int(input("Enter value: "))
        l1.insert_at_end(value)
    elif choice == '3':
        l1.display()
    elif choice == '4':
        l1.reverse_list()
        print("List reversed.")
    elif choice == '5':
        break
    else:
        print("Invalid choice")