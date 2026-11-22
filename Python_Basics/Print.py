# How to Print in Python

print("Hello World")
print("Today I am starting Python")

print("Hi My name is Abhi")
print(7)
print(7.8)

# sep - what goes BETWEEN the values (default is a space)
print("hello", 1, 1.6, True, sep="/")      # hello/1/1.6/True
print("hello", 1, 1.6, True, sep="*")      # hello*1*1.6*True

# end - what goes at the END (default is a new line "\n")
print("loading", end="...")
print("done")                               # loading...done

a = "Abhi"
b = "Shravana"
print(a + " " + b)                          # Abhi Shravana

num = 1234.12234
print(f"the number is {num:.2f}")           # the number is 1234.12

print("line_1\nline_2\nline_3")

print("""hello
my name is abhi
I am learning python because i want to become
top software engineers in the world""")

age = 25

# without using the f-string - print adds a space between each value
print("my name is", a, "my age is", age)            # my name is Abhi my age is 25

# using the format method
print("My name is {}, My age is {}".format(a, age)) # My name is Abhi, My age is 25

# using the fstring (the best and most used way)
print(f"hello my name is {b}")

# defining the variables
u_name = "abhi"
l_name = 'gowda'
u_age = 25
u_active = True

# we use "," to put commas as the thousand separator
l_num = 98765342.22
print(f'{l_num:,.1f}')      # 98,765,342.2

# "sep" is a parameter of print(), it has no meaning INSIDE an f-string,
# here it's just printed as normal text
print(f"{u_name},{l_name},{u_age},sep='|'")     # abhi,gowda,25,sep='|'

# "sep" works when we pass separate values to print
print(u_name, l_name, u_age, sep="|")           # abhi|gowda|25

# "f" is the format specifier for float, by default it shows 6 decimal places

x = 4.56789456
print(f"{x:f}")     # 4.567895  rounded to 6 places, the extra digits are lost

y = 5.6783
print(f"{y:f}")     # 5.678300  padded with 2 zeros to make 6 places

z = 45.7896
print(f"{z:.2f}")   # 45.79     ".2" means round off to 2 decimal places

a = 12345678
print(f"{a:,}")     # 12,345,678   it's an integer, so plain {a:,} is enough

# % is a type, like f. It multiplies by 100 and adds the % sign.
print(f"{0.18:%}")     # 18.000000%    default 6 decimals, same rule as f
print(f"{0.18:.0%}")   # 18%
print(f"{0.1834:.1%}") # 18.3%         useful for growth rates, conversion rates in reports

# zero-padding - the width counts EVERY character, including the "."
print(f"{12345:05d}")   # 12345    (already 5 digits, no padding)
print(f"{7:05d}")       # 00007    (1 digit, so 4 zeros are added)
print(f"{123:05d}")     # 00123    (3 digits, so 2 zeros are added)
print(f"{3.14159:07.3f}") # 003.142  (rounded to 3 places = 5 characters "3.142", so 2 zeros are padded to make 7)

# alignment - < left, > right, ^ center, the number is the width
# very useful to print a clean table / report in the terminal
print(f"{'name':<10}|{'sales':>10}")
print(f"{'abhi':<10}|{1500.5:>10,.2f}")
print(f"{'ravi':<10}|{98000:>10,.2f}")
# name      |     sales
# abhi      |  1,500.50
# ravi      | 98,000.00

# debugging shortcut - "=" prints the expression and its value (python 3.8+)
rows = 120
print(f"{rows = }")             # rows = 120
print(f"{rows * 2 = }")         # rows * 2 = 240

# printing dictionaries / JSON nicely
# API responses and LLM (GenAI) responses come as JSON, which python reads as a dict
import json
response = {"model": "llm", "usage": {"input_tokens": 12, "output_tokens": 40}, "ok": True}
print(response)                         # all on one line, hard to read when it's big
print(json.dumps(response, indent=2))   # pretty printed with 2-space indentation
# {
#   "model": "llm",
#   "usage": {
#     "input_tokens": 12,
#     "output_tokens": 40
#   },
#   "ok": true          <- note: JSON uses lowercase true / false and null
# }

# print vs logging
# print() is fine for learning and quick checks. In real data pipelines / ETL jobs we use
# the logging module instead - it adds time, level (INFO / WARNING / ERROR) and can write to files
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.info("loaded %s rows", rows)        # 2026-11-22 10:15:00,123 INFO loaded 120 rows
logging.warning("5 rows had missing values")
