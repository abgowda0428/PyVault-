# Single Inheritance

class Animal:

    def __new__(cls,*args,**kwargs):
        print("Empty Object is Created")
        return super().__new__(cls)

    def __init__(self,name):
        self.UserName = name
    
    def ShowUser(self):
        print(f"This is the User logged into Our System, {self.UserName}")
     
class Dog(Animal):

    def ShowDogUser(self):
        print(f"This is the Dog Owner, {self.UserName}")     

d = Dog("abhishek")

d.ShowUser() #From Father
d.ShowDogUser() #From Own

# MultiLevel Inheritance

class Grandfather:
    def property(self):
        print("Land from Grandfather")

class Father(Grandfather):
    def business(self):
        print("Business from Father")

class Son(Father):
    def skills(self):
        print("Son has coding skills")

s = Son()
s.property()   # from Grandfather
s.business()   # from Father
s.skills()     # own

#  Multiple Inheritance

class Mother:
    def cooking(self):
        print("Mother cooks")

class Father:
    def driving(self):
        print("Father drives")

class Child(Mother, Father):
    def playing(self):
        print("Child plays")

c = Child()
c.cooking()
c.driving()
c.playing()


# Hierarchical Inheritance

class Parent:
    def show(self):
        print("I am Parent")

class Child1(Parent):
    def child1_fun(self):
        print("I am Child1")

class Child2(Parent):
    def child2_fun(self):
        print("I am Child2")

c1 = Child1()
c1.show()
c1.child1_fun()

c2 = Child2()
c2.show()
c2.child2_fun()

# Hybrid Inheritance

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):  # inherits from both B and C (multiple)
    pass
