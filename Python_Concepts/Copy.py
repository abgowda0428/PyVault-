# Copying in python

import copy

a = [1, 2, [3, 4]]  # List with a nested list
b = copy.copy(a)    # Shallow copy
print(b)            # Output: [1, 2, [3, 4]] 

b.append(5)         # Change top level of b

print(a)            # Output: [1, 2, [3, 4]]  (a unchanged here)
print(b)            # Output: [1, 2, [3, 4], 5]

# But nested changes affect both!

b[2].append(6)      # Change the inner list via b
print(a)            # Output: [1, 2, [3, 4, 6]]  (a changed too!)
print(b)            # Output: [1, 2, [3, 4, 6], 5]

# Shollow Copy in the Class

import copy

class Dog:
    def __init__(self, name, toys):
        self.name = name
        self.toys = toys  # toys is a list (nested)

dog1 = Dog("Buddy", ["ball", "bone"])
dog2 = copy.copy(dog1)  # Shallow copy

dog2.name = "Max"       # Change top-level attribute
print(dog1.name)        # Output: Buddy (unchanged)
print(dog2.name)        # Output: Max

dog2.toys.append("rope")  # Change nested list
print(dog1.toys)          # Output: ['ball', 'bone', 'rope'] (changed!)
print(dog2.toys)          # Output: ['ball', 'bone', 'rope']