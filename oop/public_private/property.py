class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # property accessor (getter method) - get the __name property
    @property
    def name(self):
        return self.__name
    
    # property modifier (setter method) - modifies the __name property
    @name.setter
    def name(self, name):
        # If the name parameter is not empty, it is assigned to the __name attribute of the object
        # Otherwise, assign the __name attribute to 'Anonymous', there are two ways of writing
        # self.__name = name if name else 'Anonymous'
        self.__name = name or 'anonymous'
    
    @property
    def age(self):
        return self.__age


stu = Student('John', 20)
print(stu.name, stu.age)    # John 20
stu.name = ''
print(stu.name)    # John
# stu.age = 30     # AttributeError: can't set attribute