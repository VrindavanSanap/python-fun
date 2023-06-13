#Code taken from chatGPT
from datetime import date

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @property
    def age(self):
        current_year = date.today().year
        return current_year - self.birth_year

# Create a Person instance
person = Person("John", 1990)

# Access the age property
print(person.age)  # Output: 33

# Update the birth year
person.birth_year = 1985

# Access the age property again
print(person.age)  # Output: 38 (updated age)
