# __slot__ in Python

# By default, 
# Python objects store their attributes (like name, age) in a dictionary called __dict__.

'''
__slots__ is a way to optimize memory usage and restrict the attributes a class can have.
Instead of using a dictionary (__dict__), __slots__ tells Python to use a fixed set of attributes,
stored internally in a more memory-efficient structure (like a tuple or array).
You define __slots__ as a class variable, listing the allowed attributes as strings in a tuple or list.
'''

# Class without __slots__
class PersonWithoutSlots:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Class with __slots__
class PersonWithSlots:
    __slots__ = ('name', 'age')  # Tuple of allowed attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Usage
person1 = PersonWithoutSlots("Alice", 30)
person2 = PersonWithSlots("Bob", 25)

# Check __dict__
print(person1.__dict__)  # Output: {'name': 'Alice', 'age': 30}
# print(person2.__dict__)  # Error: 'PersonWithSlots' object has no attribute '__dict__'

# Try adding a new attribute
person1.email = "alice@example.com"  # Works
print(person1.__dict__)  # Output: {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}

# person2.email = "bob@example.com"  # Error: 'PersonWithSlots' object has no attribute 'email'


# Inheretence

class Base:
    def __init__(self):
        self.base_attr = "I am base"

class Derived(Base):
    __slots__ = ('name',)  # Only 'name' is in slots
    def __init__(self, name):
        super().__init__()
        self.name = name

# Usage
obj = Derived("Alice")
print(obj.name)  # Output: Alice
print(obj.base_attr)  # Output: I am base
print(obj.__dict__)  # Output: {'base_attr': 'I am base'}
# obj.new_attr = "test"  # Works because __dict__ exists


# Using json

import json

# Mixin for serialization
class JSONMixin:
    def to_json(self):
        return json.dumps(self.__dict__)
    
    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

# Person class with __slots__
class Person(JSONMixin):
    __slots__ = ('name', 'age')  # Use a tuple to define allowed attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Usage
person = Person("Alice", 30)
# json_data = person.to_json()  # Error: 'Person' object has no attribute '__dict__'

# Fix the mixin to work with __slots__
class JSONMixinForSlots:
    def to_json(self):
        # Manually create a dictionary since __dict__ doesn't exist
        return json.dumps({slot: getattr(self, slot) for slot in self.__slots__})
    
    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

# Person class with updated mixin
class PersonWithSlots(JSONMixinForSlots):
    __slots__ = ('name', 'age')
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Usage
person = PersonWithSlots("Alice", 30)
json_data = person.to_json()
print(json_data)  # Output: {"name": "Alice", "age": 30}

new_person = PersonWithSlots.from_json(json_data)
print(new_person.name, new_person.age)  # Output: Alice 30

# Memory Consomption

import sys

class PersonWithoutSlots:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonWithSlots:
    __slots__ = ('name', 'age')
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create instances
p1 = PersonWithoutSlots("Alice", 30)
p2 = PersonWithSlots("Bob", 25)

# Compare memory usage
print(sys.getsizeof(p1.__dict__))  # Size of the dictionary
print(sys.getsizeof(p2))  # Size of the object (no __dict__)

# https://grok.com/share/c2hhcmQtMw%3D%3D_5951c01c-c769-46f9-b2de-7d21f214ac47     refernce for the Chat