# class Customer:
#     def __init__(self,name,house):
#         self.name = name + "'s"
#         self.house = house

# def main():
#     student = get_student()
#     print(f"{student.name} {student.house}")

# def get_student():
#     name = input("Name : ")
#     house = input("House :")
#     object = ClassName()
#     return Customer()

# main()


class Student:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"{self.name}"
    
student = Student("Maung Maung")
student.name = "Aung Aung"
print(student.name)