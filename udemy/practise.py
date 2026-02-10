import random

#Decorators
'''def func():
    return 1
number = func
print(number())'''

#returning a func by writing a func in return value
'''def hello(name='Nithya'):
    print('The hello() function has been executed')

    def greet():
        return '\t This is the greet() function inside hello'
    def welcome():
        return '\t This is welcome() inside hello'
    
    print('I am going to return a function')
    
    if name == 'Nithya':
        return greet
    else:
        return welcome
    #print(greet())
    #print(welcome())
    #print('This is the end of the hello fucntion')
my_new_func = hello()
print(my_new_func())'''

'''def cool():
    def super_cool():
        return 'I am very cool'
    return super_cool
some_func = cool()
print(some_func())'''

#passing function as argument into another function
'''def hello():
    return 'Hi Nithya'
def other(some_def_func):
    print('Other code runs here')
    print(some_def_func())
other(hello)'''

#this is decorator function
'''def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before the original fucntion')
        original_func()
        print('Some extra code, after the original function')
    return wrap_func

@new_decorator
def func_needs_decorator(): #this is main or original function to which decorator is written
    print('I want to be decorator!')
func_needs_decorator()'''


#Generators
#create a generator that generates the squares of numbers upto some number N
'''def gensquares(N):
    for i in range(N):
        yield i ** 2
for number in gensquares(10):
    print(number)'''

#Create a generator that yields "n" random numbers between a low and high number (that are inputs).
'''def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)
for number in rand_num(3,20,5):
    print(number)'''

#use the iter() func to convert the string below into an iterator
'''s = 'hello'
s_iter = iter(s)
print(s_iter)'''

#collections
'''from collections import Counter
my_list = [1,1,2,3,2,3,2,1,3,2,4,5,4]
print(Counter(my_list))'''

'''from datetime import date
d = date(2005,1,11) #date(year,month,date)
print(d)'''

#math module
'''mport math
value = 5.99
print(math.floor(value))
print(math.ceil(value))
print(round(5.5)) #round() uses a rule that it rounds to nearest even number
print(math.pi)
print(math.nan)
print(math.inf)
print(math.e)
print(math.log(math.e)) #math.log returns a float value
print(math.sin(1))'''

#random module
import random
random.seed(10)
print(random.randint(0,100))
mylist = list(range(0,20))
print(random.choice(mylist))
#sample with replacement
print(random.choices(population=mylist,k=10))
#sample without replacement
print(random.sample(population=mylist,k=10))
random.shuffle(mylist)
print(mylist)
print(random.uniform(a=0,b=10))

