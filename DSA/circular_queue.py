class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.q = [None] * size
        self.rear = -1
        self.front = -1
    def enqueue(self,value):
        if (self.rear + 1) % self.size == self.front:
            print('Queue is full')
            return
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
    def dequeue(self):
        if self.front == -1:
            print('Queue is empty')
            return
        value = self.q[self.front]
        self.q[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return value
    def peek(self):
        return self.q[self.front]
    def display(self):
        print(self.q)

c1 = CircularQueue(5)
while True:
    print('1. Enqueue')
    print('2. Dequeue')
    print('3. Display')
    print('4. Peek')
    print('5. Exit')

    option = input('Enter a new option: ')
    if option == '1':
        value = int(input('Enter a value: '))
        c1.enqueue(value)
    elif option == '2':
        c1.dequeue()
    elif option == '3':
        c1.display()
    elif option == '4':
        print(c1.peek())
    elif option == '5':
        exit()
    else:
        print('Enter valid option')