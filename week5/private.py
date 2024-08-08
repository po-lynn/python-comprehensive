class Student:
   def __init__(self, name):
       self.__name = name

   def study(self, course):
       print(f'{self.__name}{course}.')

student_obj = Student('John')
student_obj.study('Python Programming')
# print(student_obj._Student__name)
# print(student_obj.__name) # AttributeError (Property Error)
