class Student:
    # constructor 
    def __init__(self, student_id, student_name):
        self.student_name = student_name
        self.student_id = student_id

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        if not student_id:
            raise ValueError("ID must be a non-empty string")
        self._student_id = student_id

    def study(self):
        print(f"Student {self.student_id} {self.student_name} is studying Python Course")

student1 = Student("", "John") # Raises ValueError
student2 = Student("002", "Maung Maung")
print(student2.student_name)
student2.study()
print(student1) # Raises AttributeError since the object is not created due to ValueError
