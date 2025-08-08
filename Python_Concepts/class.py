class Manufacturer:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def Maunfacture(self):
        print(f"Manufacturer: {self.name}, Country: {self.country}")

 
class Car(Manufacturer):
    
    def __init__(self,name, country, model, year):
        super().__init__(name, country)
        self.model = model
        self.year = year

    def display_info(self):
        super().Maunfacture()
        print(f"Car Model: {self.model}, Year: {self.year}")

car_1 = Car("Toyota", "Japan", "Camry", 2020)
car_1.display_info()

class Parent():
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Child(Parent):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def display(self):
        super().display()
        print(f"School: {self.school}")

'''
super() is used to call the parent class method and access its attributes 
without explicitly naming the parent class.
and it is used in both __init__ and __new__ methods.
when we Intilize the Constructor Method in the Child Class.
and multiple inheritance is also used in this code.
for maintaining the sequence of Excetion of Class Accordinly.
'''