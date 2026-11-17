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

# using the sys libary to see the memory allocation for the primitive data types
print(sys.getsizeof(qty))
print(sys.getsizeof(row_loaded))

# float - the number with the decimal point

unit_weigjt= 18.98
weight_kg= 12.78
whole_but_float= 4.0
tiny= 0.2
sci= 1.5e3                  # scientific notation = 1.5 × 10³

print(unit_weigjt)
print(weight_kg)
print(whole_but_float)
print(tiny)
print(sci)

print(sys.getsizeof(unit_weigjt))
print(sys.getsizeof(sci))

# bool - it will hold the two options True or Flase

is_active = True
in_stock = False

print(is_active)           
print(type(is_active))     
print(type(in_stock))      
print(isinstance(is_active, bool))   

# none - special value meaning no value / nothing here , its nonetype
supplier = None

print(supplier)            # None
print(type(supplier))      # <class 'NoneType'>
print(supplier is None)    # True   <- the way to check for None

# typecasting - converting a value from one type to another using int(),float(),str() and bool()

print(int("120"))       # 120
print(float("4.5"))     # 4.5
print(str(120))         # 120   (it's now text; check with type)
print(type(str(120)))   # <class 'str'>

print(int(3.9))         # 3      truncates, does NOT round
print(int(-3.9))        # -3
print(float(5))         # 5.0
print(int(True))        # 1
print(int(" 480 "))     # 480    spaces around digits are allowed
print(str(None))        # None   (but it's now the text "None")

# bool rules 

print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False   empty string
print(bool(" "))      # True    not empty
print(bool("False"))  # True    ← any non-empty text is True
print(bool(None))     # False

