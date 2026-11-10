# Abstraction

from abc import ABC,abstractmethod

class Animal(ABC):

    def __init__(self,name,age):
        self.animal_name = name
        self.animal_age = age
     
    @abstractmethod
    def Animal_Sound(self):
        print(f"Dog Name : {self.animal_name}..")

class Dog(Animal):

    def Animal_Sound(self):
        super().Animal_Sound()
        print("Bow ....Bow")
        print(f"Dog: {self.animal_age}")


    def Animal_Age(self):
        print(f"The age of Animal ,{self.animal_age}..")

Small_Dog = Dog("Pinkky",25)

Small_Dog.Animal_Sound()
Small_Dog.Animal_Age()

# Using With @Property

class Vehical(ABC):

    def __init__(self,Weels,Seats):
        self.Car_Weels = Weels
        self.Car_Seat = Seats
    
    @property
    @abstractmethod
    def Car_details(self):
        pass

    @Car_details.setter
    @abstractmethod
    def Car_details(self):
        pass

class TATA(Vehical):

    @property
    def Car_details(self):
        return (self.Car_Seat, self.Car_Weels)
    
    @Car_details.setter
    def Car_details(self,value):
        self.Car_Seat = value
    
Car_1 = TATA(4,8)
print(Car_1.Car_details)

#@property in an abstract method means that subclasses must implement ...
# a read-only attribute-like interface for that method, so you can retrieve its ...
# value without calling it with parentheses.
# This is an attribute, not a regular method → you’ll access it like obj.name instead of obj.name().

        