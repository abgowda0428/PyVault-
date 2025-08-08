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

class Lokesh:

    def __new__(cls,*args,**kwargs):
        print("Object Created")
        return super().__new__(cls)
    
    def __init__(self,*args,**kwargs):
         print("Values added To the Object")
         self.name = args
         self.ex = kwargs

    def __str__(self):
        m =  self.name[0]
        return str(m)

    def __add__(self,Others):
        list_val = self.ex["c"]
        tup_val = self.name[0]

        total = 0
        
        for value in list_val:
            total += value + tup_val       
        return total   

    def run(self):
        return f"{self.name}and this is lokesh Ex {self.ex}"

s = Lokesh(5,b = "abhishek", c= [1,2,3,4,5])

print(s)
print(s + 0)

