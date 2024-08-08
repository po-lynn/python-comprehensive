
numbers = [1,2,3,4,5]
squared_numbers = map(lambda x: x*x,numbers)
print(list(squared_numbers))

def multiply(x, y):
    return x * y

num1 = [1, 2, 3, 4, 5]
num2 = [10, 20, 30, 40, 50]
result = map(lambda x,y: x*y, num1, num2)
print(list(result)) 
