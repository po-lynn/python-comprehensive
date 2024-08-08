class ParentClass:
    def print_me(self):
        print("Parent Method")
 
class ChildClass(ParentClass):
    def print_me(self):
        print("Child Method")
        super().print_me() 

child_instance = ChildClass()
child_instance.print_me()


class ParentClass:
    def print_me(self):
        print("Parent")
 
class ChildClass(ParentClass):
    def print_me(self):
        print("Child")
 
child_instance = ChildClass()
child_instance.print_me()