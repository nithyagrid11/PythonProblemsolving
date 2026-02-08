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
def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before the original fucntion')
        original_func()
        print('Some extra code, after the original function')
    return wrap_func

@new_decorator
def func_needs_decorator(): #this is main or original function to which decorator is written
    print('I want to be decorator!')
func_needs_decorator()
