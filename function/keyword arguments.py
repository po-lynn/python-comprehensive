def is_triangle(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and b + c > a and a + c > b


# Call the function to pass in parameters without specifying the parameter name 
# and place it according to the position
print(is_triangle(1, 2, 3))
# The call function passes in the parameters in order in the form of
#  "parameter name = parameter value"
print(is_triangle(a=1, b=2, c=3))
# The calling function passes the parameters in the form 
# of "parameter name = parameter value" out of order
print(is_triangle(c=3, a=1, b=2))


#Parameters without parameter names 
# (positional parameters) must appear before parameters with parameter names 
# (keyword parameters) ,

def calc(*args, **kwargs):
    result = 0
    for arg in args:
        if type(arg) in (int, float):
            result += arg
    for value in kwargs.values():
        if type(value) in (int, float):
            result += value
    return result


print(calc())                  # 0
print(calc(1, 2, 3))           # 6
print(calc(a=1, b=2, c=3))     # 6
print(calc(1, 2, c=3, d=4))    # 10


