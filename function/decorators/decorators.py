"""
def simple_func():
    #do simple stuff
    return something
"""

"""def func():
    return 1
func()

func

def hello():
    return "Hello"

hello()
hello

greet = hello

greet()

del hello

greet()"""
# ==========================
"""
def hello(name="GCA"):
    print('The hello function() has been executed!')
    
    def greet():
        return '\t This is the greet() func inside hello'
    
    def welcome():
        return '\t This is welcome() inside hello'
    
    print(greet())
    print(welcome())
    print('This is the end of the hello function!')
    # greet and welcome function define inside of the hello funciton
    # only work inside of function
    # if you try outside of the function greet() got error

hello()

"""

def hello(name="GCA"):
    print('The hello function() has been executed!')
    
    def greet():
        return '\t This is the greet() func inside hello'
    
    def welcome():
        return '\t This is welcome() inside hello'
    
    print("I am going to return function!!")
    # to work outside of function
    if name == "GCA":
        return greet
    else: return welcome


my_new_func = hello("GCA")

print(my_new_func ) #<function hello.<locals>.greet at 0x7fc3e16cd280>

print(my_new_func()) # return a function within another function

#=========================================

def cool():
    def super_cool():
        return 'I am very cool!'
    return super_cool

some_func = cool()

#=========================================
def hello():
    return "Hi GCA"

def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func())

other(hello)

#==================Decoractor=======================

def new_decorator(original_func):

    def wrap_func():
        print('Some extra code, before the original function')
        original_func()
        print('Some extra code, after the original function!')

    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!")

decorated_func = new_decorator(func_needs_decorator)

decorated_func()

#==================================
@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()