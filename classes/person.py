class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        """Getter method for the name attribute."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter method for the name attribute."""
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

p = Person(3) #TypeError: Name must be a string
print(p.name) # Output: "Maung Maung"
p.name = "Aung Aung"
print(p.name) # Output: "Aung Aung"
