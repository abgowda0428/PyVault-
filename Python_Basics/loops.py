# loops in python - repeat a block of code again and again
# two kinds of loops - for loop and while loop

# for loop - goes through each item of a sequence (list, string, range, tuple, dict, set)

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)        # apple, banana, mango  (one per line)

# looping over a string - each character one by one
for ch in "abhi":
    print(ch)           # a, b, h, i

# range() - generates a sequence of numbers
# range(stop)               0 to stop-1
# range(start, stop)        start to stop-1
# range(start, stop, step)  jumps by step, the stop value is never included

for i in range(5):
    print(i)            # 0 1 2 3 4

for i in range(2, 6):
    print(i)            # 2 3 4 5

for i in range(0, 10, 2):
    print(i)            # 0 2 4 6 8

for i in range(5, 0, -1):
    print(i)            # 5 4 3 2 1   negative step counts down

# looping with the index - enumerate()
for index, fruit in enumerate(fruits):
    print(index, fruit)             # 0 apple, 1 banana, 2 mango

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)             # 1 apple, 2 banana, 3 mango

# avoid range(len(...)) - it works, but enumerate is cleaner and less error-prone
# for i in range(len(fruits)):
#     print(i, fruits[i])

# looping over a dictionary
student = {"name": "Abhi", "age": 25}
for key in student:
    print(key)                      # name, age
for value in student.values():
    print(value)                    # Abhi, 25
for key, value in student.items():
    print(key, value)               # name Abhi, age 25

# looping over records - a list of dicts
# this is how rows look when you read JSON, call an API, or fetch rows from a database
orders = [
    {"id": 1, "city": "Bangalore", "amount": 500},
    {"id": 2, "city": "Mysore", "amount": 300},
    {"id": 3, "city": "Bangalore", "amount": 200},
]
total_amount = 0
for order in orders:
    total_amount += order["amount"]
print(total_amount)                 # 1000

# group by + sum with a loop (the same idea as SQL GROUP BY / pandas groupby)
sales_by_city = {}
for order in orders:
    city = order["city"]
    sales_by_city[city] = sales_by_city.get(city, 0) + order["amount"]
print(sales_by_city)                # {'Bangalore': 700, 'Mysore': 300}

# looping over two lists together - zip()
names = ["Abhi", "Ravi"]
marks = [90, 80]
for name, mark in zip(names, marks):
    print(name, mark)               # Abhi 90, Ravi 80
# zip stops at the SHORTEST list silently - use strict=True (python 3.10+) to raise an error
# if the lengths don't match, e.g. column names vs row values
columns = ["id", "name"]
row = [7, "abhi"]
print(dict(zip(columns, row, strict=True)))     # {'id': 7, 'name': 'abhi'}

# while loop - keeps running as long as the condition is True

count = 1
while count <= 5:
    print(count)        # 1 2 3 4 5
    count += 1          # don't forget to update, or the loop never ends (infinite loop)

# sum of numbers from 1 to 10
total = 0
n = 1
while n <= 10:
    total += n
    n += 1
print(total)            # 55

# break - stops the loop immediately
for i in range(1, 10):
    if i == 5:
        break
    print(i)            # 1 2 3 4

# continue - skips the rest of this round and goes to the next one
for i in range(1, 6):
    if i == 3:
        continue
    print(i)            # 1 2 4 5

# pass - does nothing, just a placeholder where a statement is needed
for i in range(3):
    pass

# else with a loop - runs only when the loop finishes WITHOUT hitting break
for i in range(1, 4):
    print(i)
else:
    print("loop completed")     # printed, because there was no break

for i in range(1, 4):
    if i == 2:
        break
else:
    print("never printed")      # skipped, because break was hit

# nested loops - a loop inside a loop, the inner one runs fully for every round of the outer one
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")   # end=" " keeps the output on the same line
    print()                     # moves to the next line
# 1 2 3
# 2 4 6
# 3 6 9

# star pattern
for i in range(1, 5):
    print("*" * i)
# *
# **
# ***
# ****

# break only stops the INNER loop in nested loops
for i in range(1, 3):
    for j in range(1, 4):
        if j == 2:
            break               # stops the j loop, the i loop keeps going
        print(i, j)             # 1 1, 2 1

# while True with break - when you don't know how many times it should run
# real use: retrying a failed API call / database connection a few times
attempt = 0
max_retries = 3
while True:
    attempt += 1
    success = attempt == 3      # pretend the call works on the 3rd try
    if success:
        print(f"connected on attempt {attempt}")    # connected on attempt 3
        break
    if attempt >= max_retries:
        print("giving up")
        break
    print(f"attempt {attempt} failed, retrying")
print("out of the loop")

# DON'T change (add / remove) a list while looping over it - items get skipped
nums = [1, 2, 2, 3]
for n in nums:
    if n == 2:
        nums.remove(n)
print(nums)                     # [1, 2, 3]   one 2 was skipped!
# build a new list instead
nums = [1, 2, 2, 3]
nums = [n for n in nums if n != 2]
print(nums)                     # [1, 3]

# batching / chunking - process big data in pieces
# used for bulk database inserts, sending records to an API, creating LLM embeddings in batches
record_ids = list(range(1, 11))     # 10 records
batch_size = 4
for start in range(0, len(record_ids), batch_size):
    batch = record_ids[start:start + batch_size]
    print(batch)                # [1, 2, 3, 4]  [5, 6, 7, 8]  [9, 10]

# list comprehension - a short way to build a list with a loop
squares = [x ** 2 for x in range(1, 6)]
print(squares)          # [1, 4, 9, 16, 25]

evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)            # [2, 4, 6, 8, 10]

# dict and set comprehensions
square_map = {x: x ** 2 for x in range(1, 4)}
print(square_map)       # {1: 1, 2: 4, 3: 9}
cities = {order["city"] for order in orders}
print(sorted(cities))   # ['Bangalore', 'Mysore']   set removes duplicates

# generator expression - same as a list comprehension but with ( )
# it gives one value at a time instead of building the full list in memory
# use it when you only need to loop once / sum, on big data
print(sum(x * x for x in range(1_000_000)))     # no million-item list is created

# any() / all() - check a condition across all the items
amounts = [500, 300, 0]
print(any(a == 0 for a in amounts))     # True   at least one zero amount
print(all(a >= 0 for a in amounts))     # True   no negative amounts (a data quality check)

# for vs while
# for   - when you know how many times, or you are going through a collection
# while - when you repeat until a condition changes
