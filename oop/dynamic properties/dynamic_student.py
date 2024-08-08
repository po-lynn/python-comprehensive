class Student:
    def __init__(self, name):
        self.name = name
student_obj = Student('John')
student_obj.sex = 'Male'
# =========== __slots__

class Student:
    __slots__ = ('name', 'age')
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student('John', 21)
stu.sex = 'Male' # AttributeError: 'Student' object has no attribute 'sex'