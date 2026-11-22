# conditional statements in python - run a block of code only when a condition is True
# if , if-else , if-elif-else , nested if , ternary (one-line if) , match-case
# python uses INDENTATION (4 spaces) to mark the block, and ":" at the end of the condition line

# if - runs the block only if the condition is True
age = 25
if age >= 18:
    print("eligible to vote")       # printed

# if-else - one of the two blocks will always run
marks = 30
if marks >= 35:
    print("pass")
else:
    print("fail")                   # fail

# if-elif-else - checks one by one from the top, runs the FIRST True block and skips the rest
score = 82
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"                     # this one runs, the checks below are skipped
elif score >= 50:
    grade = "C"
else:
    grade = "F"
print(grade)                        # B

# the order of elif matters - put the strictest condition first
# if score >= 50 was on top, 82 would wrongly get "C"

# multiple conditions with and , or , not
temp = 28
is_raining = False

if temp > 25 and not is_raining:
    print("go for a walk")          # printed

day = "sunday"
if day == "saturday" or day == "sunday":
    print("weekend")                # weekend

if day in ("saturday", "sunday"):   # cleaner way using "in"
    print("weekend")

# chained comparison
if 18 <= age <= 60:
    print("working age")            # printed

# nested if - an if inside another if
has_ticket = True
has_id = False
if has_ticket:
    if has_id:
        print("enter")
    else:
        print("show your id")       # show your id
else:
    print("buy a ticket")

# truthy and falsy - any value can be used as a condition
# falsy : False, None, 0, 0.0, "" , [] , {} , () , set()
# truthy: everything else
name = ""
if name:
    print("hello", name)
else:
    print("name is empty")          # name is empty

items = [1, 2, 3]
if items:
    print("list has items")         # printed

# checking for None - use "is", not "=="
supplier = None
if supplier is None:
    print("no supplier")            # no supplier

# careful - "if value:" and "if value is not None:" are NOT the same
quantity = 0                        # a real value, zero items
if quantity:
    print("has quantity")           # NOT printed, because 0 is falsy
if quantity is not None:
    print("quantity is present")    # printed - use this when 0 / "" are valid values

# missing keys in a dict - use .get() instead of an if check (API / JSON data often has missing fields)
user = {"name": "abhi"}
email = user.get("email")           # None, no KeyError
print(email or "no email")          # no email
# user["email"]                     # KeyError: 'email'

# checking the type before using a value
amount = "500"
if isinstance(amount, str):
    amount = float(amount)
print(amount)                       # 500.0

# data quality checks - the same if / elif logic every ETL job uses to accept or reject rows
rows = [
    {"id": 1, "email": "a@x.com", "amount": 250},
    {"id": 2, "email": None, "amount": 100},
    {"id": 3, "email": "c@x.com", "amount": -40},
]
valid, rejected = [], []
for row in rows:
    if row["email"] is None:
        rejected.append((row["id"], "missing email"))
    elif row["amount"] < 0:
        rejected.append((row["id"], "negative amount"))
    else:
        valid.append(row)
print(len(valid))                   # 1
print(rejected)                     # [(2, 'missing email'), (3, 'negative amount')]

# guard clause - check the bad case first and exit early, instead of deep nested ifs
def load_file(path):
    if not path.endswith(".csv"):
        return "skipped: not a csv"
    if path.startswith("tmp_"):
        return "skipped: temp file"
    return f"loading {path}"

print(load_file("orders.csv"))      # loading orders.csv
print(load_file("notes.txt"))       # skipped: not a csv

# ternary operator (conditional expression) - value_if_true if condition else value_if_false
num = 7
result = "even" if num % 2 == 0 else "odd"
print(result)                       # odd

status = "adult" if age >= 18 else "minor"
print(status)                       # adult

# pass - placeholder when a block is needed but you have nothing to write yet
if age > 100:
    pass                            # without pass this would be an IndentationError

# common mistakes
# if age = 18:      # SyntaxError, "=" assigns, use "==" to compare
# if age > 18       # SyntaxError, missing ":" at the end
# if x == 1 or 2:   # always True! it means (x == 1) or (2), and 2 is truthy
#                   # correct way: if x == 1 or x == 2:  /  if x in (1, 2):

# match-case (python 3.10+) - python's version of the "switch-case" statement
# compares one value against several patterns, the first matching case runs
# there is NO fall-through like in C/Java, so no "break" is needed

command = "stop"
match command:
    case "start":
        print("starting")
    case "stop":
        print("stopping")           # stopping
    case "pause":
        print("pausing")
    case _:                         # "_" is the default case, matches anything
        print("unknown command")

# matching several values in one case with "|" (or)
day = "sat"
match day:
    case "sat" | "sun":
        print("weekend")            # weekend
    case "mon" | "tue" | "wed" | "thu" | "fri":
        print("weekday")
    case _:
        print("invalid day")

# guard - an extra "if" condition on a case
marks = 72
match marks:
    case m if m >= 90:
        print("A")
    case m if m >= 75:
        print("B")
    case m if m >= 35:
        print("pass")               # pass
    case _:
        print("fail")

# matching numbers / http status codes
status_code = 404
match status_code:
    case 200:
        print("OK")
    case 400 | 404:
        print("client error")       # client error
    case 500:
        print("server error")
    case _:
        print("something else")

# matching the structure of a list / tuple and capturing the values
point = (0, 5)
match point:
    case (0, 0):
        print("origin")
    case (0, y):
        print(f"on the y-axis at {y}")      # on the y-axis at 5
    case (x, 0):
        print(f"on the x-axis at {x}")
    case (x, y):
        print(f"point at {x}, {y}")

cmd = ["move", "left", 3]
match cmd:
    case ["quit"]:
        print("bye")
    case ["move", direction, steps]:
        print(f"moving {direction} {steps} steps")  # moving left 3 steps
    case ["move", *_]:
        print("move needs a direction and steps")
    case _:
        print("unknown")

# matching a dictionary - only the listed keys need to be present
user = {"role": "admin", "name": "abhi"}
match user:
    case {"role": "admin", "name": name}:
        print(f"welcome admin {name}")      # welcome admin abhi
    case {"role": "guest"}:
        print("welcome guest")
    case _:
        print("access denied")

# GenAI example - an LLM API response can contain different kinds of content blocks,
# e.g. plain text, or a request to call one of your tools / functions
# match-case is a clean way to handle each shape
blocks = [
    {"type": "text", "text": "Total sales are 1000"},
    {"type": "tool_use", "name": "run_sql", "input": {"query": "SELECT 1"}},
]
for block in blocks:
    match block:
        case {"type": "text", "text": text}:
            print("model said:", text)                      # model said: Total sales are 1000
        case {"type": "tool_use", "name": tool, "input": args}:
            print(f"model wants to call {tool} with {args}")
            # model wants to call run_sql with {'query': 'SELECT 1'}
        case _:
            print("unknown block")

# matching by type
value = 3.14
match value:
    case int():
        print("integer")
    case float():
        print("float")              # float
    case str():
        print("string")
    case _:
        print("other type")

# before python 3.10, a dictionary was used as a simple switch
def get_day_name(n):
    days = {1: "mon", 2: "tue", 3: "wed"}
    return days.get(n, "invalid")   # second argument is the default

print(get_day_name(2))              # tue
print(get_day_name(9))              # invalid

# small practice program - simple calculator
a, b, op = 10, 3, "/"
match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b != 0:
            print(round(a / b, 2))  # 3.33
        else:
            print("cannot divide by zero")
    case _:
        print("invalid operator")
