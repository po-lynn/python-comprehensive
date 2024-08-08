class Student:
    pass
    # def __init__(self,name,house):
    #     if not name:
                # return None       # Student object is already created you 
                                    # should not do that it is too late
    #     self.name = name + "'s"
    #     self.house = house

def main():
    student = get_student()
    # student.name = ""
    print(f"{student.name} from {student.house}")

def get_student():
   
    student = Student()
    student.name = input("Name : ")
    student.house = input("House :")
    # student = Student(name,house)

    return student

main()
