class Student:
    
    def __init__(self,name,house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    try:
         student.name = ""
    except ValueError as e:
         print(str(e))
    print(f"{student.name} from {student.house}")

@property
def name(self):
    return self._name

@name.setter
def name(self,name):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string")
    self._name = name


def get_student():

    name = input("Name : ")
    house = input("House :")
    return Student(name,house)

main()
