class Person:
    """Humanity"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name}eating.')
    
    def sleep(self):
        print(f'{self.name}is sleeping.')


class Student(Person):
    """Student class"""
    
    def __init__(self, name, age):
        # super(Student, self).__init__(name, age)
        super().__init__(name, age)
    
    def study(self, course_name):
        print(f'{self.name}Currently learning{course_name}.')


class Teacher(Person):
    """Teacher class"""

    def __init__(self, name, age, title):
        # super(Teacher, self).__init__(name, age)
        super().__init__(name, age)
        self.title = title
    
    def teach(self, course_name):
        print(f'{self.name}{self.title}Teacher class{course_name}.')



stu1 = Student('John', 21)
stu2 = Student('Honey', 22)
teacher = Teacher('Steve', 35, 'Associate Professor')
stu1.eat()
stu2.sleep()
teacher.teach('Python program design')
stu1.study('Python program design')