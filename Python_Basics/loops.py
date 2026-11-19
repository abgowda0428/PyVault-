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

# looping over a dictionary
student = {"name": "Abhi", "age": 25}
for key in student:
    print(key)                      # name, age
for key, value in student.items():
    print(key, value)               # name Abhi, age 25

# looping over two lists together - zip()
names = ["Abhi", "Ravi"]
marks = [90, 80]
for name, mark in zip(names, marks):
    print(name, mark)               # Abhi 90, Ravi 80

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

# while True with break - when you don't know how many times it should run
while True:
    number = 7
    if number > 5:
        break
print("out of the loop")

# list comprehension - a short way to build a list with a loop
squares = [x ** 2 for x in range(1, 6)]
print(squares)          # [1, 4, 9, 16, 25]

evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)            # [2, 4, 6, 8, 10]

# for vs while
# for   - when you know how many times, or you are going through a collection
# while - when you repeat until a condition changes
