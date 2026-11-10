# Static Methods

# These  Methods behave like normal functions Inside the Class .
'''
A static method in Python is a method inside a class that does not need:
   **self (object reference)
   **cls (class reference)
It behaves just like a normal function, but is placed inside a class for organization.
'''

class Company:

    @staticmethod
    def Shope_Floor(a,b):
        return f"These are machines in shopeFloor {a}:{b}"
    
C = Company()  #Using Object

print(C.Shope_Floor(1,2)) 
    
print(Company.Shope_Floor("Mazzak","Tusnami"))   #Using Class

# Class Method It will inhert the from base class and take the Varible reference form the sub class if 
# present or It will refer to Base Class Varible.

# Class Method

class Dog:
   
    Bark = "Bow Bow..."

    @classmethod
    def Make_sound(cls):
        return cls.Bark
    
class PitBull(Dog):
    
    Bark = "Bow Bow Bow ....."

print(Dog.Make_sound())
print(PitBull.Make_sound())

# Factory Method

class Birday:

    def __init__(self,name,age):
        self.UserName = name
        self.UserAge = age
    
    @classmethod
    def BirthdayUser(cls,Name,Birthday_Year):
        current_Year = 2025
        age = current_Year - Birthday_Year
        return cls(Name,age)

P1 = Birday("yogesh",30)
P2 = Birday.BirthdayUser("bhrath",2000)

print(P1.UserName,P1.UserAge)
print(P2.UserName,P2.UserAge)


"""he provided code defines a Birday class with an __init__ method (the standard constructor)
 and a class method from BirthdayUser (an alternative or "custom" constructor).
 It then creates two instances: p1 using the standard constructor and p2 using the custom class method.
 """
# then returns a new instance by calling cls(name, age)—which is equivalent to Birday(name, age). 
# This doesn't create a "custom instance" type;
#  it's just a convenient alternative way to instantiate the class without directly providing age.