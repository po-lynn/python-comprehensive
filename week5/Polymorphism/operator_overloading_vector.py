class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()
    
    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2  # Calls the __add__ method
print(v3)  # Prints "(4, 6)"

v4 = v2 - v1  # Calls the __sub__ method
print(v4)  # Prints "(2, 2)"

v5 = v1 * 3  # Calls the __mul__ method
print(v5)  # Prints "(3, 6)"

print(v1 == v2)  # Calls the __eq__ method and prints "False"
print(v1 < v2)  # Calls the __lt__ method and prints "True"
