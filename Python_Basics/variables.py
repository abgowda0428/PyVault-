# Constant goes in the uppercase
GST_RATE = 0.18

# Define the varibles(use the snake_case for the defining the variable)
u_name = "abhi"
l_name = 'gowda'
u_age = 25
u_active = True

# naming rules: letters, digits, underscore; can't start with a digit; case-sensitive
# can't use keywords like if, for, class, True
# booleans read better with is_/has_ prefix

# swapping the variable using the temp variable 

a= 123
b= 456

temp= a
a= b 
print(a,b)

# we can use this method also for swapping the variable without the third glass
a, b = b, a

# multiple assignment
a, b, c = 1, 2, 3

# checking the type of the variable 

print(type(a))
print(type(u_active))