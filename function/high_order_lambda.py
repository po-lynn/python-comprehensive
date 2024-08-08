def calc(*args, init_value, op, **kwargs):
    result = init_value
    for arg in args:
        if type(arg) in (int, float):
            result = op(result, arg)
    for value in kwargs.values():
        if type(value) in (int, float):
            result = op(result, value)
    return result


def add(x, y):
    return x + y


def mul(x, y):
    return x * y

print("===========================")

print(calc(1, 2, 3, init_value=0, op=add, x=4, y=5))      # 15
print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=mul))    # 120

print("===========================")

import operator
print(calc(1, 2, 3, init_value=0, op=operator.add, x=4, y=5))      # 15
print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=operator.mul))    # 120

#==================Map====================

# example 1
def square(num):
    return num **2

my_nums = [1,2,3,4,5]
for item in map(square,my_nums):
    print(item)

list(map(square,my_nums))   
# example 2
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'Even'
    else:
        return mystring[0]

names = ['Maung','John','Andy']
list(map(splicer,names))
#=============================================
def is_even(num):
    return num % 2 == 0


def square(num):
    return num ** 2


numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(square, filter(is_even, numbers1)))
print(numbers2)    # [144, 64, 3600, 2704]

numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = [num ** 2 for num in numbers1 if num % 2 == 0]
print(numbers2)    # [144, 64, 3600, 2704]

numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers1)))
print(numbers2)    # [144, 64, 3600, 2704]


#-------------------
def calc(*args, init_value=0, op=lambda x, y: x + y, **kwargs):
    result = init_value
    for arg in args:
        if type(arg) in (int, float):
            result = op(result, arg)
    for value in kwargs.values():
        if type(value) in (int, float):
            result = op(result, value)
    return result


#Call the calc function, using the default values of init_value and op
print(calc(1, 2, 3, x=4, y=5))    # 15
# Call the calc function and assign a value to the op parameter through the lambda function
print(calc(1, 2, 3, x=4, y=5, init_value=1, op=lambda x, y: x * y))    # 120


import operator, functools

# One line of code defines a function to find factorial
fac = lambda num: functools.reduce(operator.mul, range(1, num + 1), 1)
# One line of code defines a function for judging prime numbers
is_prime = lambda x: x > 1 and all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

# Invoke the Lambda function
print(fac(10))        # 3628800
print(is_prime(9))    # False