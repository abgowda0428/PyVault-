# Data Classes In Python

from dataclasses import dataclass, field

@dataclass(order=True,eq=True) 
 
# By using this we Can to customize the,
# Other properties in the @dataClass which will directly pass when we use the data class

class Animal:

    #  These Variables are called as Fields
     
    name : str = field(default="Prajeet")  #Here we are making them as Default Parameters
    age : int = field(default = 18)
    Address : list = field(default_factory=list)

    def AnimalSound(self):
        return f"The animals Name is {self.name}, and animal age is {self.age}."
    
a = Animal("Bhrath",Address=[1,2,3,4,5,6])

print(a.age,a.name)

print(a.AnimalSound())



