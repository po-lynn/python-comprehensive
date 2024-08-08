class Student:
    """student"""

    def __init__(self, name, age):
        """initialization method"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """study"""
        print(f'{self.name}Currently learning{course_name}.')

    def play(self):
        """play"""
        print(f'{self.name}playing game.')
    
    def __repr__(self):
        return f'{self.name}: {self.age}'


stu1 = Student('Student1', 40)
print(stu1)        # Student1: 40
students = [stu1, Student('Student2', 36), Student('Student3', 25)]
print(students)    # [Student1: 40, Student2: 36, Student3: 25]