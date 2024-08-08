class Student:
    # constructor 
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    def study(self):
        print(f'{self.name} is studying Python Course.')

# student1 = Student('') # Raises ValueError
student1 = Student('John') # Raises ValueError
student1.name = ''
print(student1) # Raises AttributeError since the object is not created due to ValueError
