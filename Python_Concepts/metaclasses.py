# MetaClass in Python

# https://grok.com/share/c2hhcmQtMw%3D%3D_4f5b7c42-acc7-4f57-a36c-ed360f8bc690  --References

'''
When you define a class like Dog, Python doesn't just magically make it exist. 
Behind the scenes, Python uses a special thing called type to create that class.
type is like a factory that builds classes. It's the default "class maker."
For example, you could even create a class without using the class keyword, by directly using type:
'''

# Creating a class dynamically using 'type'
# type(class_name, (parent_classes), {attributes_and_methods})
Cat = type("Cat", (), {"meow": lambda self: print("Meow!")})

my_cat = Cat()
my_cat.meow()  # Output: Meow!

# https://grok.com/share/c2hhcmQtMw%3D%3D_05b58847-42a1-4e86-b073-ae2fe5d30a8c --- Complete Reference

# Meta Classes Full Imoplemented Code

import datetime

class TimestampMeta(type):
    def __new__(cls, name, bases, dct):
        dct['created_at'] = datetime.datetime.now()
        dct['info'] = lambda cls: print(f"Class {cls.__name__} created at {cls.created_at}")
        return super().__new__(cls, name, bases, dct)

class Student(metaclass=TimestampMeta):
    pass

Student.info()  # Output: Class Student created at 2025-08-14 10:10:56.789012

"""
** cls : refence to MetaClass.
** name : Refer to Class Name.
** bases : Refer to Parent Classes if Inhertation Happens Means.
** dct : refer to for Creating Class attributes.

"""

# A metaclass is a special kind of class that creates and controls other classes.