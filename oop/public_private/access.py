class Student:

    def __init__(self, name):
        self.__name = name

    def study(self, course_name):
        print(f'{self.__name}{course_name}.')

student_obj = Student('John')
student_obj.study('Python Programming')
print(student_obj._Student__name)