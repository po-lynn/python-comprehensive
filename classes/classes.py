# print(type(10)) #<class 'int'>
# print(type("Hello World")) #<class 'str'>
# print(type([])) #<class 'list'>
# print(type(list()))#<class 'list'>
# print(type({})) #<class 'dict'>

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def square(cls, side_length):
        return cls(side_length, side_length)

# Usage
square = Rectangle.square(5)
print(square.width) # 5
print(square.height) # 5

class Math:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y

# Usage
result = Math.add(1, 2)
print(result) # 3

result = Math.multiply(2, 3)
print(result) # 6
