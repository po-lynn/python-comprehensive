"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

people = [
    Person("John", 25),
    Person("Doe", 30),
    Person("Steve", 20)
]

sorted_people = sorted(people)

for person in sorted_people:
    print(person.name, person.age)
"""
# ==============================
"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

people = [
    Person("Alice", 25),
    Person("Bob", 30),
    Person("Charlie", 20)
]

sorted_people = sorted(people, key=lambda x: x.age)

for person in sorted_people:
    print(person.name, person.age)
"""
#========================================================================================
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

people = [
    Person("Alice", 25),
    Person("Bob", 30),
    Person("Charlie", 20)
]

min_person = min(people)

print("The youngest person is", min_person.name, "who is", min_person.age, "years old.")
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

people = [
    Person("Alice", 25),
    Person("Bob", 30),
    Person("Charlie", 20)
]

sorted_people = sorted(people, key=lambda x: x.age)

for person in sorted_people:
    print(person)
    
Person(name='Charlie', age=20)
Person(name='Alice', age=25)
Person(name='Bob', age=30)
