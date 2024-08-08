class Student:
    
    def __init__(self, name, house):
        self.name = name
        self.house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name must be a non-empty string")
        self._name = name

# Example usage
s = Student("Student1", "south okkalapa")
print(s.name)  # Output: Student1

# Attempt to set an invalid name
try:
    s.name = ""
except ValueError as e:
    print(str(e))  # Output: Name must be a non-empty string
