# string in python - a sequence of characters inside quotes ('', "", ''' ''', """ """)
# strings are IMMUTABLE - once created, you can't change a character in place

first_name = 'Abhi'
last_name = "Gowda"

# string concatination
full_name = first_name + last_name
print(full_name)            # AbhiGowda

# space between the concatination variable
full_name = first_name + " " + last_name
print(full_name)            # Abhi Gowda

# length function for string
print(len(full_name))       # 10   (the space is also counted)

# indexing - starts from 0 from the left, and -1 from the right
#  A  b  h  i     G  o  w  d  a
#  0  1  2  3  4  5  6  7  8  9
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(full_name[1])         # b    forward indexing
print(full_name[-9])        # b    reverse indexing
print(full_name[-1])        # a    last character
# print(full_name[20])      # IndexError: string index out of range

# slicing - [start:stop:step] , the stop index is NOT included
print(full_name[0:3])       # Abh   forward slicing
print(full_name[-5:-1])     # Gowd  reverse slicing
print(full_name[:4])        # Abhi  start is 0 by default
print(full_name[5:])        # Gowda goes till the end by default
print(full_name[::2])       # Ah od every 2nd character (index 0, 2, 4, 6, 8)
print(full_name[::-1])      # adwoG ihbA  reverses the string
print(full_name[2:50])      # hi Gowda  slicing never throws an error, it just stops at the end

# immutability
# full_name[0] = 'a'        # TypeError: 'str' object does not support item assignment
full_name = 'a' + full_name[1:]     # make a new string instead
print(full_name)            # abhi Gowda

# multi-line string
address = """Bangalore
Karnataka
India"""
print(address)

# escape characters
print("line_1\nline_2")     # \n new line
print("name\tage")          # \t tab space
print("He said \"hi\"")     # \" double quote inside double quotes
print('It\'s python')       # \' single quote inside single quotes
print("C:\\new_folder")     # \\ prints a single backslash
print(r"C:\new_folder")     # r"" raw string, the backslash is not treated as escape

# repetition and membership
print("ha" * 3)             # hahaha
print("bhi" in "abhi")      # True
print("xyz" not in "abhi")  # True

# case methods - every method returns a NEW string, the original is unchanged
name = "abhishek gowda"
print(name.upper())         # ABHISHEK GOWDA
print(name.lower())         # abhishek gowda
print(name.title())         # Abhishek Gowda   first letter of every word
print(name.capitalize())    # Abhishek gowda   only the first letter
print(name)                 # abhishek gowda   original is still the same
# to use the result, store it:  name = name.title()

# removing spaces (very useful while cleaning data)
raw = "   data engineer   "
print(raw.strip())          # "data engineer"     removes both sides
print(raw.lstrip())         # "data engineer   "  removes the left side
print(raw.rstrip())         # "   data engineer"  removes the right side
print("###abhi###".strip("#"))  # abhi  can remove any character, not just spaces

# methods can be chained - a common way to clean a messy value from a CSV / form
city = "  BANGALORE \n"
print(city.strip().title())     # Bangalore

# removeprefix / removesuffix (python 3.9+) - removes an exact piece from the start / end
path = "s3://my-bucket/raw/orders.csv"
print(path.removeprefix("s3://"))           # my-bucket/raw/orders.csv
print("orders.csv".removesuffix(".csv"))    # orders
# don't use strip for this - strip(".csv") removes the CHARACTERS . c s v from both ends
print("sales.csv".strip(".csv"))            # ale    (the "s" at the start AND end got removed too!)

# finding and counting
text = "python is easy and python is fun"
print(text.find("python"))      # 0     index of the first match
print(text.find("java"))        # -1    not found gives -1
print(text.index("is"))         # 7     same as find, but throws ValueError if not found
print(text.rfind("python"))     # 19    searches from the right
print(text.count("python"))     # 2
print(text.startswith("py"))    # True
print(text.endswith("fun"))     # True

# replace
print(text.replace("python", "sql"))        # sql is easy and sql is fun
print(text.replace("python", "sql", 1))     # sql is easy and python is fun  only the first one

# split and join - string <-> list
csv_row = "CSK,MI,BNG"
teams = csv_row.split(",")
print(teams)                    # ['CSK', 'MI', 'BNG']
print("hello world".split())    # ['hello', 'world']  splits on spaces by default
print("a  b   c".split())       # ['a', 'b', 'c']     no-argument split also handles extra spaces
print("a,,b".split(","))        # ['a', '', 'b']      with a separator, empty values are kept
# maxsplit - split only the first n times
log_line = "ERROR: db timeout: retry later"
print(log_line.split(":", 1))   # ['ERROR', ' db timeout: retry later']
print(path.split("/")[-1])      # orders.csv   last part of a path = the file name
# NOTE: for real CSV files use the csv module or pandas - a plain split(",") breaks when
# a value itself contains a comma, like "Bangalore, India"
print(" | ".join(teams))        # CSK | MI | BNG
print("".join(["a", "b", "c"])) # abc
# join only works on strings - convert numbers first
print(",".join(str(n) for n in [1, 2, 3]))     # 1,2,3

# building a big string - collect the parts in a list and join once at the end
# "+=" in a loop creates a new string every time (strings are immutable), which is slow
parts = []
for i in range(3):
    parts.append(f"row{i}")
print("\n".join(parts))

# checking methods - all return True / False
print("12345".isdigit())        # True
print("abhi".isalpha())         # True
print("abhi25".isalnum())       # True   letters or digits
print("   ".isspace())          # True
print("ABHI".isupper())         # True
print("abhi".islower())         # True

# zero padding - used for ids, month numbers in file paths like 2026/07/01
print("7".zfill(3))             # 007

# formatting strings
age = 25
print("My name is " + first_name + " and age is " + str(age))   # + needs str(), it won't join str and int
print("My name is {} and age is {}".format(first_name, age))
print(f"My name is {first_name} and age is {age}")              # f-string, the best way
print(f"{first_name!r}")        # 'Abhi'   shows the quotes, handy for debugging
print(f"{age = }")              # age = 25  prints the variable name and value

# templates with named placeholders - fill the same text with different data
# this is exactly how prompt templates for LLMs (GenAI) are built
PROMPT = """You are a data analyst.
Summarise the sales for {city} in {month}.
Answer in {max_words} words or less."""
print(PROMPT.format(city="Bangalore", month="March", max_words=50))

row = {"city": "Mysore", "month": "April", "max_words": 30}
print(PROMPT.format(**row))     # ** unpacks the dict into named arguments

# to print a real { or } inside an f-string / format, double it: {{ }}
# needed when your prompt asks the LLM to reply in JSON
user_id = 7
print(f'Reply only as JSON like {{"user_id": {user_id}, "score": 0}}')
# Reply only as JSON like {"user_id": 7, "score": 0}

# looping over a string
for ch in "abhi":
    print(ch)                   # a, b, h, i

# encoding - str (text) <-> bytes
# files, network calls and APIs send BYTES, python works with STR, utf-8 is the standard encoding
data = "café"
raw_bytes = data.encode("utf-8")
print(raw_bytes)                # b'caf\xc3\xa9'
print(raw_bytes.decode("utf-8"))    # café
print(len(data), len(raw_bytes))    # 4 5   é takes 2 bytes in utf-8
# always pass encoding="utf-8" when opening text files: open("file.csv", encoding="utf-8")

# ord() and chr() - character <-> unicode number
print(ord("A"))                 # 65
print(chr(97))                  # a

# comparing strings - compared character by character using the unicode values
print("apple" < "banana")       # True
print("Apple" < "apple")        # True   uppercase letters come before lowercase
print("abhi" == "Abhi")         # False  case-sensitive
print("abhi".lower() == "Abhi".lower())     # True  compare ignoring the case
