class EmptyQueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []
        self.front = 0
    def is_empty(self):
        return self.front == len(self.items)
    def size(self):
        return len(self.items)
    def enqueue(self,item):
        return self.items.append(item)
    def dequeue(self):
        if self.is_empty:
            raise EmptyQueueError('queue is empty')
        x = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        return x
    def peek(self):
        if self.is_empty:
            raise EmptyQueueError('queue is empty')
        return self.items[self.front]
    def display(self):
        print(self.items)