#sum
sum = lambda num : num +10
print(sum(40))

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