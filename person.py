
# In Python, you can create property getters and setters using the @property and @<property_name>.setter decorators. 
# Here's an example:

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


person = Person("Alice", 30)
print(person.name)  # Output: Alice

person.name = "Bob"
print(person.name)  # Output: Bob

person.age = 25
print(person.age)  # Output: 25
person.age = -1  # Raises a ValueError