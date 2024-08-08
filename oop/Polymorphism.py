class ParentClass:
    def print_self(self):
        print('A')
 
class ChildClass(ParentClass):
    def print_self(self):
        print('B')
 
obj_A = ParentClass()
obj_B = ChildClass()
 
obj_A.print_self() # => A
obj_B.print_self() # => B
