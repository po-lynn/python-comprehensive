from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """staff"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """settlement monthly salary"""
        

class Manager(Employee):
    """Department manager"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """programmer"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):
    """Seller"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05 #5%
    

emps = [
    Manager('Su'), Programmer('Honey'), Manager('Po'), 
    Programmer('Mike'), Salesman('Steve'), Programmer('John'),
]
for emp in emps:
    if isinstance(emp, Programmer):
        emp.working_hour = int(input(f'please enter {emp.name} Working hours this month: '))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'please enter {emp.name} Sales this month: '))
    print(f"{emp.name}This month's salary is: ${emp.get_salary():.2f} Dollar")