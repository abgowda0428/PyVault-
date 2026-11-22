# list in python - an ordered, MUTABLE collection, written with square brackets []
# it can hold duplicates and mixed types

lst = ['CSK', 'MI', 'BNG']

print(type(lst))                # <class 'list'>

# creating lists
empty = []
also_empty = list()
numbers = [10, 20, 30, 40, 50]
mixed = ["abhi", 25, 5.8, True, None]
nested = [[1, 2], [3, 4]]
from_string = list("abhi")
from_range = list(range(1, 6))

print(mixed)                    # ['abhi', 25, 5.8, True, None]
print(from_string)              # ['a', 'b', 'h', 'i']
print(from_range)               # [1, 2, 3, 4, 5]
print(len(numbers))             # 5

# indexing - same as strings, 0 from the left and -1 from the right
print(numbers[0])               # 10
print(numbers[-1])              # 50
print(nested[1][0])             # 3   first [1] picks [3, 4], then [0] picks 3
# print(numbers[10])            # IndexError: list index out of range

# slicing - [start:stop:step] , stop is not included, it gives back a NEW list
print(numbers[1:4])             # [20, 30, 40]
print(numbers[:2])              # [10, 20]
print(numbers[::2])             # [10, 30, 50]
print(numbers[::-1])            # [50, 40, 30, 20, 10]   reversed copy

# lists are mutable - we can change the items in place (strings can't do this)
lst[0] = 'RCB'
print(lst)                      # ['RCB', 'MI', 'BNG']
numbers[1:3] = [200, 300]       # replace a slice
print(numbers)                  # [10, 200, 300, 40, 50]

# adding items
teams = ['CSK', 'MI']
teams.append('RCB')             # adds ONE item at the end
print(teams)                    # ['CSK', 'MI', 'RCB']
teams.insert(1, 'KKR')          # adds at the given index
print(teams)                    # ['CSK', 'KKR', 'MI', 'RCB']
teams.extend(['SRH', 'DC'])     # adds every item of another list
print(teams)                    # ['CSK', 'KKR', 'MI', 'RCB', 'SRH', 'DC']

# append vs extend
a = [1, 2]
a.append([3, 4])
print(a)                        # [1, 2, [3, 4]]   the whole list goes in as one item
b = [1, 2]
b.extend([3, 4])
print(b)                        # [1, 2, 3, 4]

# removing items
teams.remove('KKR')             # removes the first matching VALUE (ValueError if not present)
print(teams)                    # ['CSK', 'MI', 'RCB', 'SRH', 'DC']
last = teams.pop()              # removes and RETURNS the last item
print(last, teams)              # DC ['CSK', 'MI', 'RCB', 'SRH']
second = teams.pop(1)           # removes and returns the item at index 1
print(second, teams)            # MI ['CSK', 'RCB', 'SRH']
del teams[0]                    # deletes by index, returns nothing
print(teams)                    # ['RCB', 'SRH']
teams.clear()                   # empties the list
print(teams)                    # []

# searching and counting
scores = [45, 78, 90, 78, 32]
print(scores.index(78))         # 1    index of the first match
print(scores.count(78))         # 2
print(90 in scores)             # True
print(100 not in scores)        # True

# sorting
scores.sort()                   # sorts IN PLACE and returns None
print(scores)                   # [32, 45, 78, 78, 90]
scores.sort(reverse=True)
print(scores)                   # [90, 78, 78, 45, 32]

marks = [45, 78, 90, 32]
print(sorted(marks))            # [32, 45, 78, 90]   sorted() returns a NEW list
print(marks)                    # [45, 78, 90, 32]   the original is unchanged

names = ["ravi", "abhi", "Kiran"]
print(sorted(names))                    # ['Kiran', 'abhi', 'ravi']  uppercase comes first
print(sorted(names, key=str.lower))     # ['abhi', 'Kiran', 'ravi']  ignores the case
print(sorted(names, key=len))           # ['ravi', 'abhi', 'Kiran']  sorts by the length

# common mistake - sort() returns None
# result = marks.sort()
# print(result)                 # None

# sorting a list of records (list of dicts) by a field - very common with JSON / API data
# key= takes a function; "lambda r: r['amount']" is a small one-line function that
# returns the amount of each record (lambda is covered in functions)
orders = [
    {"id": 1, "amount": 500},
    {"id": 2, "amount": 1200},
    {"id": 3, "amount": 300},
]
top_orders = sorted(orders, key=lambda r: r["amount"], reverse=True)
print(top_orders[:2])           # [{'id': 2, 'amount': 1200}, {'id': 1, 'amount': 500}]  top 2
print(max(orders, key=lambda r: r["amount"]))   # {'id': 2, 'amount': 1200}

# reversing
marks.reverse()                 # in place
print(marks)                    # [32, 90, 78, 45]

# removing duplicates
ids = [3, 1, 3, 2, 1]
print(list(set(ids)))           # [1, 2, 3]   set removes duplicates, but the ORDER is not guaranteed
print(list(dict.fromkeys(ids))) # [3, 1, 2]   removes duplicates AND keeps the original order

# built-in functions on lists
nums = [4, 8, 15, 16, 23, 42]
print(sum(nums))                # 108
print(min(nums))                # 4
print(max(nums))                # 42
print(sum(nums) / len(nums))    # 18.0   average

# joining and repeating lists
print([1, 2] + [3, 4])          # [1, 2, 3, 4]
print([0] * 5)                  # [0, 0, 0, 0, 0]

# copying - "=" does NOT copy, both names point to the same list
original = [1, 2, 3]
same = original
same.append(4)
print(original)                 # [1, 2, 3, 4]   original changed too!

original = [1, 2, 3]
copy_1 = original.copy()        # these three make a real (shallow) copy
copy_2 = original[:]
copy_3 = list(original)
copy_1.append(4)
print(original)                 # [1, 2, 3]   unchanged

# shallow copy keeps the inner lists shared - use deepcopy for nested lists
import copy
matrix = [[1, 2], [3, 4]]
shallow = matrix.copy()
deep = copy.deepcopy(matrix)
matrix[0][0] = 99
print(shallow)                  # [[99, 2], [3, 4]]  inner list is shared
print(deep)                     # [[1, 2], [3, 4]]   fully independent

# unpacking
x, y, z = [1, 2, 3]
print(x, y, z)                  # 1 2 3
first, *rest = [10, 20, 30, 40]
print(first, rest)              # 10 [20, 30, 40]

# looping over a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
for i, fruit in enumerate(fruits):
    print(i, fruit)             # 0 apple, 1 banana, 2 mango

# list comprehension - [expression for item in iterable if condition]
squares = [n ** 2 for n in range(1, 6)]
print(squares)                  # [1, 4, 9, 16, 25]
evens = [n for n in range(10) if n % 2 == 0]
print(evens)                    # [0, 2, 4, 6, 8]
lower_teams = [t.lower() for t in ['CSK', 'MI', 'BNG']]
print(lower_teams)              # ['csk', 'mi', 'bng']
labels = ["pass" if m >= 35 else "fail" for m in [45, 20, 90]]
print(labels)                   # ['pass', 'fail', 'pass']

# 2D list (list of lists) - like rows and columns of a table
table = [
    ["id", "name", "age"],
    [1, "abhi", 25],
    [2, "ravi", 28],
]
for row in table:
    print(row)
print(table[1][1])              # abhi   row 1, column 1
header, *data_rows = table      # split the header row from the data rows
print(header)                   # ['id', 'name', 'age']
print([r[1] for r in data_rows])    # ['abhi', 'ravi']   pick one "column"

# flatten a list of lists into one list
batches = [[1, 2], [3, 4], [5]]
flat = [item for batch in batches for item in batch]
print(flat)                     # [1, 2, 3, 4, 5]

# performance note - append() and pop() at the END are fast
# insert(0, x) and pop(0) at the START are slow on big lists (every item has to shift)
# for a queue use collections.deque, it has fast popleft()
from collections import deque
queue = deque(["job1", "job2"])
queue.append("job3")
print(queue.popleft())          # job1

# empty list is False, non-empty list is True
print(bool([]))                 # False
print(bool([0]))                # True   it has one item, even if that item is 0
