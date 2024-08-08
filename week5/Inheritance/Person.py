class Person:
   """Humanity"""

   def __init__(self, name, age):
       self.name = name
       self.age = age
  
   def eat(self):
       print(f'{self.name} is eating.')
  
   def sleep(self):
       print(f'{self.name} is sleeping.')


class Student(Person):
   """Student class"""
  
   def __init__(self, name, age):
    #    super(Student, self).__init__(name, age) # old version   
       super().__init__(name, age)    # python 3
  
   def study(self, course_name):
       print(f'{self.name} is currently learning {course_name}.')

class Teacher(Person):
   """Teacher class"""

   def __init__(self, name, age, title):
       # super(Teacher, self).__init__(name, age) # old version  
       super().__init__(name, age) # python 3
       self.title = title
  
   def teach(self, course_name):
       print(f'{self.name} {self.title} teach  {course_name} course.')


stu1 = Student('John', 21)
stu1.eat()
stu1.study('Python Programming')

teacher = Teacher('Steve', 35, 'Professor')

teacher.teach('Python Programming')

