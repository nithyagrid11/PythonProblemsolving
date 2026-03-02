class Node:
        def __init__(self,value):
            self.value = value
            self.next = None
class Linkedlist:
    def __init__(self):
         self.start = None
    def insert_at_end(self,value):
        new_node = Node(value)
        if self.start is None:
             self.start = new_node
             return
        p = self.start
        while p.next is not None:
             p = p.next
        p.next = new_node
    def palindrome_linkedlist(self):
        list1 = []
        curr = self.start
        while curr:
            list1.append(curr.value)
            curr = curr.next
        return list1 == list1[::-1]
l1 = Linkedlist()
l1.insert_at_end(5)
l1.insert_at_end(2)
l1.insert_at_end(3)
l1.insert_at_end(2)
l1.insert_at_end(5)
print(l1.palindrome_linkedlist())