'''class Student:
    def __init__(self,name):
        self.name = name
    
    def greet(self):
        print("hello",self.name)


n1 = Student('Nithya')
print(n1.name)
n1.greet()'''

'''class Book:
    def __init__(self,title,price):
        self.title = title
        self.price = price
    def method(self):
        print('Titel: ',self.title)
        print('Price: ',self.price)
b1 = Book('Harry Potter',400)
b1.method()'''

'''class User:
    total_users = 0
    def __init__(self):
        User.total_users += 1
u1 = User()
u2 = User()
u3 = User()
print(User.total_users)'''

class Phone:
    brand = 'Samsung'
    def __init__(self,model):
        self.model = model
p1 = Phone('S21')
p2 = Phone('S22')
p1.brand = 'Apple'
print(p1.brand)
print(p2.brand)