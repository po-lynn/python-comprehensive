class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet tweet!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

class AnimalShelter:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        for animal in self.animals:
            print(animal.name + ": " + animal.speak())

    def list_dogs(self):
        for animal in self.animals:
            if isinstance(animal, Dog):
                print(animal.name + ": " + animal.speak())

    def list_cats(self):
        for animal in self.animals:
            if isinstance(animal, Cat):
                print(animal.name + ": " + animal.speak())

    def list_birds(self):
        for animal in self.animals:
            if isinstance(animal, Bird):
                print(animal.name + ": " + animal.speak())

    def list_cows(self):
        for animal in self.animals:
            if isinstance(animal, Cow):
                print(animal.name + ": " + animal.speak())

    def find_animal_by_name(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal

    def remove_animal_by_name(self, name):
        animal = self.find_animal_by_name(name)
        if animal is not None:
            self.animals.remove(animal)


shelter = AnimalShelter()
shelter.add_animal(Dog("Buddy"))
shelter.add_animal(Cat("Whiskers"))
shelter.add_animal(Bird("Tweety"))
shelter.add_animal(Cow("Bessie"))
shelter.list_animals()
# Output: "Buddy: Woof!", "Whiskers: Meow!", "Tweety: Tweet tweet!", "Bessie: Moo!"
shelter.list_dogs()
# Output: "Buddy: Woof!"
shelter.list_cats()
# Output: "Whiskers: Meow!"
shelter.list_birds()
# Output: "Tweety: Tweet tweet!"
shelter.list_cows()
# Output: "Bessie: Moo!"
shelter.remove_animal_by_name("Whiskers")
shelter.list_animals()
# Output: "Buddy: Woof!", "Tweety: Tweet tweet!", "Bessie: Moo!"
