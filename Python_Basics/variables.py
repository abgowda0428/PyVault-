# variables - a name that points to a value (object) stored in memory

# Constant goes in the uppercase (python doesn't block changing it, it's just a convention)
GST_RATE = 0.18
MAX_RETRIES = 3

# Define the variables (use snake_case for variable names)
u_name = "abhi"
l_name = 'gowda'
u_age = 25
u_active = True

# naming rules: letters, digits, underscore; can't start with a digit; case-sensitive
# can't use keywords like if, for, class, True
# booleans read better with is_ / has_ prefix  ->  is_active, has_header
# use meaningful names in data code         ->  total_sales, not ts / x1

import keyword
print(keyword.kwlist)       # the full list of reserved keywords

# DON'T use built-in names as variables - it hides the built-in function
# list = [1, 2, 3]          # now list() stops working in this file
# sum = 10                  # now sum([1, 2]) gives TypeError
# also avoid: str, int, dict, type, id, input, max, min, len, file, json
# same idea applies to FILE names - a file called string.py or json.py hides python's own module

# python is dynamically typed - the same variable can point to a different type later
value = 10
print(type(value))          # <class 'int'>
value = "ten"
print(type(value))          # <class 'str'>

# type hints - tell the reader (and tools) what type is expected
# python does NOT enforce them at runtime, but they are used everywhere in modern code:
# FastAPI, pydantic (data validation), dataclasses, and LLM structured outputs
table_name: str = "orders"
row_count: int = 0
is_loaded: bool = False
discount: float | None = None   # "float or None" (python 3.10+ syntax)

# swapping the variable using the temp variable

a = 123
b = 456

temp = a
a = b
b = temp
print(a, b)                 # 456 123

# python way - swap without the third variable
a, b = b, a
print(a, b)                 # 123 456

# multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)              # 1 2 3

# same value to many variables
p = q = r = 0
print(p, q, r)              # 0 0 0
# careful: with a list, all names point to the SAME list
s1 = s2 = []
s1.append(1)
print(s2)                   # [1]   s2 changed too (more on this in list.py)

# variables are references - two names can point to the same object
n1 = "abhi"
n2 = n1
print(id(n1) == id(n2))     # True

# checking the type of the variable

print(type(a))              # <class 'int'>
print(type(u_active))       # <class 'bool'>

# delete a variable
del temp
# print(temp)               # NameError: name 'temp' is not defined

# secrets (passwords, database urls, API keys for OpenAI / Claude etc) must NEVER be
# written directly in the code - the code goes to GitHub and anyone can read it.
# store them in environment variables (or a .env file that's in .gitignore) and read them:
import os
api_key = os.getenv("LLM_API_KEY")              # None if it's not set
db_host = os.getenv("DB_HOST", "localhost")     # second value is the default
print(api_key is None)                          # True (unless you have set it)
print(db_host)                                  # localhost
