class Student:
    
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing Name")
        self.name = name + "'s"
        self.house = house

def main():
    student = get_student()
    student.name = ""
    print(f"{student.name} from {student.house}")

def get_student():

    name = input("Name : ")
    house = input("House :")
    return Student(name,house)

main()
