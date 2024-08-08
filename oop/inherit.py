class ParentClass:
    def print_me(self):
        print("Parent Method")
 
class ChildClass(ParentClass):
    def print_me(self):
        print("Child Method")
        super().print_test() 

child_instance = ChildClass()
child_instance.print_test()