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
        return self.Make_Sound(self.UserName)


D = Dog("abhi","malur") 

print(D.DogSound())