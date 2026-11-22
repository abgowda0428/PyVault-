# primitive datatypes - int, float, str, bool, None
# (list, tuple, dict, set are collection types - covered in their own files)
import sys

u_name = "abhi"         # str   (assigning with the double quote)
l_name = 'gowda'        # str   (assigning with the single quote, both are the same)
u_age = 25              # int   (NOTE: 25. with a dot would make it a float 25.0)
u_weight = 105.78       # float
u_active = True         # bool
u_dob = None            # NoneType - means "no value / unknown"
                        # None is NOT 0, NOT False and NOT "" (empty string) - it is its own thing

# to print the memory location (identity) of the object
print(id(u_name))

# to check the type of the variable
print(type(u_name))     # <class 'str'>
print(type(u_dob))      # <class 'NoneType'>

# ------------------------------------------------------------------
# int - whole number, can be +, - or 0
# ------------------------------------------------------------------

qty = 100
change = -5
zero = 0
row_loaded = 10000

print(qty)
print(change)
print(zero)
print(row_loaded)
print(type(change))                 # <class 'int'>
print(isinstance(qty, str))         # False
print(isinstance(row_loaded, int))  # True   isinstance is the preferred way to check types in real code

# python won't allow a leading 0 in an int like 008, it throws a SyntaxError
# underscores can be used to make big numbers readable, python ignores them
rows_in_table = 1_000_000
print(rows_in_table)                # 1000000

# python int has NO size limit (unlike int32 / int64 in SQL, Java, numpy)
print(2 ** 100)                     # 1267650600228229401496703205376
# NOTE for data work: pandas / numpy / databases DO use fixed sizes (int64), so very
# large values can overflow there even though plain python is fine

# using the sys library to see the memory used by the object (in bytes)
print(sys.getsizeof(qty))           # 28
print(sys.getsizeof(row_loaded))    # 28

# ------------------------------------------------------------------
# float - a number with a decimal point
# ------------------------------------------------------------------

unit_weight = 18.98
weight_kg = 12.78
whole_but_float = 4.0
tiny = 0.2
sci = 1.5e3                         # scientific notation = 1.5 × 10³

print(unit_weight)
print(weight_kg)
print(whole_but_float)
print(tiny)
print(sci)                          # 1500.0

print(sys.getsizeof(unit_weight))   # 24
print(sys.getsizeof(sci))           # 24

# IMPORTANT - floats are not exact, they are stored in binary
print(0.1 + 0.2)                    # 0.30000000000000004
print(0.1 + 0.2 == 0.3)             # False  never compare floats with ==

import math
print(math.isclose(0.1 + 0.2, 0.3)) # True   the right way to compare floats

# for money / prices use Decimal (this is why SQL has a DECIMAL / NUMERIC type)
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))      # 0.3   exact
# pass a STRING to Decimal - Decimal(0.1) would copy the float's binary error

# round() uses "banker's rounding" - .5 goes to the nearest EVEN number
print(round(2.5))                   # 2   (not 3!)
print(round(3.5))                   # 4
print(round(3.14159, 2))            # 3.14

# special float values - very common in data analytics (pandas uses NaN for missing values)
nan = float("nan")                  # nan = "Not a Number"
inf = float("inf")
print(nan == nan)                   # False  NaN is not equal to anything, even itself
print(math.isnan(nan))              # True   the right way to check for NaN
print(inf > 10 ** 100)              # True

# ------------------------------------------------------------------
# bool - holds one of two values, True or False (capital T / F)
# ------------------------------------------------------------------

is_active = True
in_stock = False

print(is_active)                    # True
print(type(is_active))              # <class 'bool'>
print(isinstance(is_active, bool))  # True

# bool is a subclass of int - True is 1 and False is 0
print(True + True)                  # 2
print(sum([True, False, True]))     # 2   handy to count how many records passed a check

# ------------------------------------------------------------------
# None - special value meaning "no value", its type is NoneType
# (it's python's version of NULL in SQL)
# ------------------------------------------------------------------

supplier = None

print(supplier)                     # None
print(type(supplier))               # <class 'NoneType'>
print(supplier is None)             # True   always use "is None", not "== None"

# ------------------------------------------------------------------
# typecasting - converting a value from one type to another
# int(), float(), str(), bool()
# in data work this happens ALL the time - CSV files, APIs, env variables all give you text
# ------------------------------------------------------------------

print(int("120"))       # 120
print(float("4.5"))     # 4.5
print(str(120))         # 120   (it's now text; check with type)
print(type(str(120)))   # <class 'str'>

print(int(3.9))         # 3      truncates, does NOT round
print(int(-3.9))        # -3
print(float(5))         # 5.0
print(int(True))        # 1
print(int(" 480 "))     # 480    spaces around the digits are allowed
print(str(None))        # None   (but it's now the text "None")

# int() can't read a decimal string directly
# print(int("4.5"))     # ValueError: invalid literal for int() with base 10: '4.5'
print(int(float("4.5")))    # 4    convert to float first
# print(int(""))        # ValueError - empty values in a CSV will crash the conversion
#                       # (we handle this with try/except, covered in exception handling)

# bool rules - only "empty" or "zero" values are False
print(bool(0))          # False
print(bool(1))          # True
print(bool(""))         # False   empty string
print(bool(" "))        # True    not empty, it has a space
print(bool("False"))    # True    any non-empty text is True
print(bool(None))       # False

# so bool("False") or bool("0") is True - to read true/false text from a file or config:
flag_text = "False"
flag = flag_text.strip().lower() in ("true", "1", "yes")
print(flag)             # False

# mutable vs immutable - an important idea for the coming topics
# immutable (can't be changed after creation): int, float, str, bool, None, tuple
# mutable   (can be changed in place)        : list, dict, set
