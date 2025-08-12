# Polymorphism in Python

# Method Overriding in Python

class Animal:

    def animal_Sound(self):
        return "Animal Makes sounds"
    
class Cat(Animal):

    def animal_Sound(self):
        return "Cat Makes MEOO..."
    
class Dog(Animal):

    def Sound(self):
        return "Dog makes Bow Bow...."
    
    def __str__(self):
        return self.Sound()
    
c = Cat()
d = Dog()

print(c.animal_Sound(),d.animal_Sound(),d.Sound())

# Method Overloading in Python

class Addition:

    def __init__(self,*args):
        self.Value_1 = args 

    def add(self):
        total = 0 
        for value in self.Value_1:              
            total += value
        return total
    
    def __str__(self):
        return f"{self.add()}"
     

addition = Addition(1,2,3,4,5,6)
print(addition)

""" 
if a single method in Python is handling many different numbers or types of parameters,
 it will almost always be written using:
Default parameters → to allow optional values
*args → to accept any number of extra positional arguments
**kwargs → to accept any number of extra keyword arguments
"""

# In this The Animal class defines a generic Animalsound method.
# Dog and Cat classes override the Animalsound method with their own implementations.
# When Animalsound is called on a list of Animal objects.but also Inherit the Properties from Parent/Base Class.
# Python determines the actual type of each object at runtime and calls the appropriate Animalsound method.

# Opeator Overloading in Python

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):  # Overloads the + operator
        return Vector(self.x + other.x, self.y + other.y)
    
    def sum(self):
        return self.x,self.y
    
    def __str__(self):  # For readable output
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Calls __add__ method
print(v3)
print(v1)

# __str__ calls when printing the Objects, and Its used for retriving the value from the Object.


# Duck Typing in Python

class Country:

    def __init__(self,*args):
        self.Value_1 = args 

    def language(self):
        total = 0 
        for value in self.Value_1:
            total += value
        return total

class State:

    def language(self):
        return "Know Kannada" 

class City:

    def __new__(cls,*args,**kwargs):
       return super().__new__(cls)
    
    def __init__(self,a,b):
        self.Value1 = a
        self.Value2 = b
        
    def language(self):
        return self.Value1 + self.Value2
    
    def Print(self):
        print("I am Back")
    
    def __str__(self):
        return self.Print()
    
def Speaklanguage(speak):
    return speak.language()

a,b = Country(1,2,3,4),State()

City(1,2).Print()

print(
Speaklanguage(a),
Speaklanguage(b),
Speaklanguage(City(1,4)))

# Duck typing in Python is a programming concept where the class of an object is less important,
#  than the methods and properties it has.
