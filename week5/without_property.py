class Student:
   def __init__(self, name):
      if not name:
            raise ValueError("Missing Name")
      self.name = name

   def study(self):
       print(f'{self.name} is studying Python Course.')

# student_obj = Student('')
student_obj = Student('John')
print(student_obj.study())
