# A mixin is a class designed to provide specific functionality (methods or attributes)
#  to other classes through multiple inheritance.

class Soundmixin:

    def Make_Sound(self,Message):
        return f"Animals make Sound,{Message}"
    

class Dog(Soundmixin):

    def __init__(self,name,place):
        self.UserName = name
        self.Userplace = place


    def DogSound(self):
        # Pass a message to the mixin's method
        return self.Make_Sound(self.UserName)


D = Dog("abhi","malur") 

print(D.DogSound())

# ----------------------------------------------------------

# Mixin class for logging
class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")

# A class that uses the mixin
class Car(LoggingMixin):
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        self.log(f"{self.brand} is driving.")

# Another class using the same mixin
class Truck(LoggingMixin):
    def __init__(self, brand):
        self.brand = brand
    
    def haul(self):
        self.log(f"{self.brand} is hauling cargo.")

# Usage
car = Car("Toyota")
car.drive()  # Output: [LOG] Toyota is driving.

truck = Truck("Volvo")
truck.haul()  # Output: [LOG] Volvo is hauling cargo.

# MIXINS for Serialization

import json

# Mixin for serialization
class JSONMixin:
    def to_json(self):
        return json.dumps(self.__dict__)
    
# Every Python object (by default) has a __dict__ attribute,
#  which is a dictionary storing all its attributes and their values.
    
    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

# A class using the mixin
class Person(JSONMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Usage
person = Person("Alice", 30)
json_data = person.to_json()
print(json_data)  # Output: {"name": "Alice", "age": 30}

new_person = Person.from_json(json_data)
print(new_person.name, new_person.age)  # Output: Alice 30