#sum
'''sum = lambda num : num +10
print(sum(40))'''

#is even
even = lambda x : x % 2 == 0
print(even(3))

#square
square = lambda x : x ** 2
print(square(4))

#max of two numbers
num = lambda a,b : max(a,b)
print(num(3,2))

#sum of three numbers
sum1 = lambda a,b,c : a + b + c
print(sum1(3,4,5))

#check string len is greater than five
str = lambda s : len(s) > 5
print(str('nithya'))

#list of integers to squares
nums = [1,2,3,4,5]
print(list(map(lambda num : num ** 2, nums)))

#extract odd numbers from a list
nums = [1,2,3,4,5,6,7,8,9,10,11]
print(list(filter(lambda num : num % 2 != 0, nums)))

#list of strings to upper case
strings = ['Nithya','college','office']
print(list(map(lambda str : str.upper(), strings)))

#sort a list of tuples based on the second element using lambda
lst = [(1,3,2),(3,2,1)]
lst.sort(key = lambda x : x[1])
print(lst)

#in a list of numbers, keep only nums divisible by 3
lst1 = [1,2,3,4,5,6,7,8,9,12]
print(list(filter(lambda num : num % 3 == 0, lst1)))

#students with marks greater than 60
students = [
    {"name": "A", "marks": 78},
    {"name": "B", "marks": 45},
    {"name": "C", "marks": 90}
]
result = list(
    map(
        lambda x : x["name"], filter(lambda x : x['marks']>60, students)
    )   
)
print(result)

#Use sort() and lambda to sort employees by salary.
employees = [
    {"id": 1, "salary": 60000},
    {"id": 2, "salary": 50000},
    {"id": 3, "salary": 40000}
]
employees.sort(key = lambda x : x["salary"])
emp = list(map(lambda x : x["id"],employees))
print(emp)

#Use map() and lambda to create a list of product names.
products = [
    {"name": "pen", "price": 10},
    {"name": "book", "price": 50},
    {"name": "bag", "price": 300}
]
print(list(map(lambda x : x["name"],products)))

#Use filter() and lambda to keep only active users.
users = [
    {"username": "x", "active": True},
    {"username": "y", "active": False},
    {"username": "z", "active": True}
]
print(list(filter(lambda x : x["active"] == True, users)))

#Use filter() and lambda to keep records with total score > 40.
records = [
    {"name": "A", "scores": [10, 20, 3]},
    {"name": "B", "scores": [5, 15, 25]}
]
print(list(filter(lambda x : sum(x["scores"]) > 40,records)))

#Find names of students whose average marks > 80.
marks = {
    "A": (78, 82, 90),
    "B": (40, 55, 60),
    "C": (88, 92, 95)
}
print(list(
    map(
        lambda x:x[0], filter(lambda x : sum(x[1]) / len(x[1]) > 80, marks.items())
    )
))

#Create a new dictionary with final price after discount.
#tuple(price,discount)
prices = {
    "pen": (10, 5),
    "book": (50, 20),
    "bag": (300, 50)
}
final_price = dict()
# discount_amount = price * (discount/100)
print(dict(map(lambda x : (
    x[0],
    x[1][0] - (x[1][0] * x[1][1] / 100)),prices.items()
    )))

#Use sorted() and lambda to sort items by the second value of the tuple.
points = {
    "A": (2, 3),
    "B": (5, 1),
    "C": (1, 4)
}
print(sorted(points.items(),key = lambda x : x[1][1]))

#Use filter() and lambda to find months where offline sales > online sales.
sales = {
    "Jan": (100, 200),
    "Feb": (150, 180),
    "Mar": (90, 220)
}
print(list(filter(lambda x : x[1][0] < x[1][1],sales.items())))