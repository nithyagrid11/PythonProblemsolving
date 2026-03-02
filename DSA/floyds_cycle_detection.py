class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
    def __init__(self):
        self.start = None
    def insert_at_end(self,value):
        new_node = Node(value)
        curr = self.start
        if self.start is None:
            self.start = new_node
            return
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = new_node
    def create_cycle(self,pos):
        if pos < 0 or self.start is None:
            return
        last = self.start
        while last.next is not None:
            last = last.next
        target = self.start
        index = 0
        while target and index < pos:
            target = target.next
            index += 1
        if target:
            last.next = target
    def cycle_detection(self):
        s = self.start
        f = self.start
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                print('Cycle detected')
                return True
        return False
l1 = Linkedlist()
l1.insert_at_end(1)
l1.insert_at_end(2)
l1.insert_at_end(3)
l1.insert_at_end(4)
l1.insert_at_end(5)
l1.create_cycle(5)
print(l1.cycle_detection())