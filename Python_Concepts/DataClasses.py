# Data Classes In Python

from dataclasses import dataclass, field
@dataclass(order=True,eq=True)
class Animal:
     
    name : str = field(default="Prajeet")
    age : int = field(default = 18)
    Address : list = field(default_factory=list)

    def AnimalSound(self):
        return f"The animals Name is {self.name}, and animal age is {self.age}."
    
a = Animal("Bhrath",Address=[1,2,3,4,5,6])

print(a.age,a.name)

print(a.AnimalSound())



