# primitive datatypes
import sys

u_name = "abhi"         #string(assigning with the double quote)
l_name = 'gowda'        #string(assigning with the single quote)
u_age = 25.             #Integer
u_weight = 105.78       #Float
u_active = True         #Bollean
u_dob = None            #Null is not zero(0), but no value , not this also because it also carry some space " "

# to print the memory location of the object in the heap
print(id(u_name))       

# to check the type of the variable
print(type(u_name))
print(type(u_dob))

# int - whole number can be anything like +,-,0 

qty= 100
change= -5
zero= 0
row_loaded = 10000

print(qty)
print(change)
print(zero)
print(row_loaded)
print(type(change))
print(type(qty))
print(type(row_loaded))
print(isinstance(qty,str))
print(isinstance(row_loaded,int))

# python won't allow the leading 0 in the int like , 008 it will throw the syntax error.

print(sys.getsizeof(qty))
print(sys.getsizeof(row_loaded))