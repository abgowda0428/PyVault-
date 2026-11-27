# set in python - an UNORDERED collection of UNIQUE items, written with curly braces {}
# it is mutable (we can add / remove), but it has no index and no duplicates

teams = {'CSK', 'MI', 'RCB', 'CSK'}

print(type(teams))              # <class 'set'>
print(len(teams))               # 3   the duplicate 'CSK' is dropped
# print(teams)                  # {'MI', 'RCB', 'CSK'}   the order can be different every run

# creating sets
empty = set()                   # {} is NOT an empty set, it is an empty dict
print(type({}))                 # <class 'dict'>
numbers = {10, 20, 30}
from_list = set([3, 1, 3, 2, 1])
from_string = set("hello")
from_range = set(range(1, 6))

print(from_list)                # {1, 2, 3}
print(sorted(from_string))      # ['e', 'h', 'l', 'o']   only one 'l', sorted() gives a fixed order
print(from_range)               # {1, 2, 3, 4, 5}

# items must be hashable (immutable) - numbers, strings, tuples are fine, lists and dicts are not
ok = {1, "abhi", 5.8, (1, 2)}
# bad = {[1, 2]}                # TypeError: unhashable type: 'list'

# True == 1 and False == 0 in python, so a set treats them as the same item
print({1, True, 0, False})      # {0, 1}

# no indexing or slicing - a set has no positions
# print(numbers[0])             # TypeError: 'set' object is not subscriptable
# to get one item, loop over it, or turn it into a list / sorted list first
print(sorted(numbers)[0])       # 10

# membership - this is what sets are best at
# "x in set" is very fast (it uses hashing), "x in list" checks every item one by one
print(20 in numbers)            # True
print(99 not in numbers)        # True

# adding items
langs = {"python", "sql"}
langs.add("spark")              # adds ONE item
print(sorted(langs))            # ['python', 'spark', 'sql']
langs.add("python")             # already there, nothing happens (no error)
print(len(langs))               # 3
langs.update(["scala", "java"]) # adds every item of another iterable (like list.extend)
print(sorted(langs))            # ['java', 'python', 'scala', 'spark', 'sql']

# add vs update with a string
s1 = set()
s1.add("abc")
print(s1)                       # {'abc'}   the whole string is one item
s2 = set()
s2.update("abc")
print(sorted(s2))               # ['a', 'b', 'c']   every character is added

# removing items
langs.remove("java")            # KeyError if the item is not present
print(sorted(langs))            # ['python', 'scala', 'spark', 'sql']
langs.discard("rust")           # same as remove, but NO error if it is missing
print(sorted(langs))            # ['python', 'scala', 'spark', 'sql']
item = langs.pop()              # removes and returns an ARBITRARY item (not "the last")
print(len(langs))               # 3
langs.clear()                   # empties the set
print(langs)                    # set()

# set operations - same as the Venn diagrams from maths
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)                    # {1, 2, 3, 4, 5, 6}   union - in a OR b
print(a.union(b))               # {1, 2, 3, 4, 5, 6}
print(a & b)                    # {3, 4}               intersection - in BOTH
print(a.intersection(b))        # {3, 4}
print(a - b)                    # {1, 2}               difference - in a but NOT in b
print(b - a)                    # {5, 6}               order matters for difference
print(a.difference(b))          # {1, 2}
print(a ^ b)                    # {1, 2, 5, 6}         symmetric difference - in one, not both
print(a.symmetric_difference(b))    # {1, 2, 5, 6}

# operator vs method - the methods accept ANY iterable, the operators need sets on both sides
print(a.union([7, 8]))          # {1, 2, 3, 4, 7, 8}
# print(a | [7, 8])             # TypeError: unsupported operand type(s) for |: 'set' and 'list'

# in-place versions change the set itself
c = {1, 2, 3}
c |= {4}                        # same as c.update({4})
print(c)                        # {1, 2, 3, 4}
c &= {2, 3, 4, 9}               # same as c.intersection_update(...)
print(c)                        # {2, 3, 4}
c -= {4}                        # same as c.difference_update({4})
print(c)                        # {2, 3}

# comparing sets
small = {1, 2}
big = {1, 2, 3}
print(small.issubset(big))      # True    every item of small is in big
print(small <= big)             # True
print(small < big)              # True    proper subset (subset AND not equal)
print(big.issuperset(small))    # True
print(big >= small)             # True
print({1, 2}.isdisjoint({3, 4}))    # True    no common items
print({1, 2, 3} == {3, 2, 1})   # True    order does not matter

# removing duplicates from a list
ids = [3, 1, 3, 2, 1]
print(list(set(ids)))           # [1, 2, 3]   duplicates gone, but the ORDER is not guaranteed
print(list(dict.fromkeys(ids))) # [3, 1, 2]   use this when the original order matters
print(len(ids) - len(set(ids))) # 2           how many duplicates there were

# data use case 1 - compare two loads of data
# which customer ids are new today, which ones disappeared, which ones are in both
yesterday = {101, 102, 103, 104}
today = {103, 104, 105, 106}
print(sorted(today - yesterday))    # [105, 106]   new records
print(sorted(yesterday - today))    # [101, 102]   missing / deleted records
print(sorted(today & yesterday))    # [103, 104]   present in both loads

# data use case 2 - schema check: are all the required columns present in the file?
required_cols = {"id", "name", "email", "created_at"}
file_cols = {"id", "name", "phone", "created_at"}
missing = required_cols - file_cols
extra = file_cols - required_cols
if missing:
    print("missing columns:", sorted(missing))  # missing columns: ['email']
print("extra columns:", sorted(extra))          # extra columns: ['phone']
print(required_cols <= file_cols)               # False   not every required column is there

# data use case 3 - fast lookups while filtering records
# build a set once, then "in" is fast even for millions of ids
blocked_users = {"u7", "u9"}
events = [
    {"user": "u1", "action": "login"},
    {"user": "u7", "action": "login"},
    {"user": "u3", "action": "buy"},
]
clean = [e for e in events if e["user"] not in blocked_users]
print([e["user"] for e in clean])   # ['u1', 'u3']

# data use case 4 - unique values in a column (like SELECT DISTINCT in SQL)
orders = [
    {"id": 1, "city": "Bengaluru"},
    {"id": 2, "city": "Mysuru"},
    {"id": 3, "city": "Bengaluru"},
]
cities = {o["city"] for o in orders}
print(sorted(cities))           # ['Bengaluru', 'Mysuru']
print(len(cities))              # 2   like COUNT(DISTINCT city)

# GenAI use case - de-duplicate the chunks returned by retrieval before building the prompt
# (several searches can bring back the same chunk; we keep each chunk once, in the original order)
retrieved = ["chunk_4", "chunk_1", "chunk_4", "chunk_7", "chunk_1"]
seen = set()
unique_chunks = []
for chunk_id in retrieved:
    if chunk_id not in seen:
        seen.add(chunk_id)
        unique_chunks.append(chunk_id)
print(unique_chunks)            # ['chunk_4', 'chunk_1', 'chunk_7']

# simple keyword overlap between a question and a document (a very basic relevance score)
question = "what is the refund policy for orders"
doc = "our refund policy allows returns on all orders within 30 days"
q_words = set(question.split())
d_words = set(doc.split())
common = q_words & d_words
print(sorted(common))           # ['orders', 'policy', 'refund']
score = len(common) / len(q_words | d_words)    # Jaccard similarity = common / all unique words
print(round(score, 2))          # 0.2    3 common words out of 15 unique words

# set comprehension - {expression for item in iterable if condition}
squares = {n ** 2 for n in range(-3, 4)}
print(sorted(squares))          # [0, 1, 4, 9]   (-3)**2 and 3**2 are both 9, kept once
emails = ["Abhi@Mail.com", "abhi@mail.com ", "ravi@mail.com"]
clean_emails = {e.strip().lower() for e in emails}
print(sorted(clean_emails))     # ['abhi@mail.com', 'ravi@mail.com']

# looping over a set - the order is not fixed, so sort it if the output order matters
for lang in sorted({"sql", "python", "spark"}):
    print(lang)                 # python, spark, sql

# copying - "=" does NOT copy, both names point to the same set
original = {1, 2, 3}
same = original
same.add(4)
print(original)                 # {1, 2, 3, 4}   original changed too!
original = {1, 2, 3}
real_copy = original.copy()     # set(original) also works
real_copy.add(4)
print(original)                 # {1, 2, 3}      unchanged

# frozenset - an IMMUTABLE set, it can't be changed after it is created
# because it is hashable, it can be a dict key or an item inside another set
fs = frozenset(["read", "write"])
# fs.add("delete")              # AttributeError: 'frozenset' object has no attribute 'add'
permissions = {
    frozenset(["read"]): "viewer",
    frozenset(["read", "write"]): "editor",
}
print(permissions[frozenset(["write", "read"])])    # editor   order does not matter
# nested = {{1, 2}}             # TypeError: unhashable type: 'set'
nested = {frozenset({1, 2}), frozenset({3})}
print(len(nested))              # 2

# built-in functions on sets
nums = {4, 8, 15, 16, 23, 42}
print(sum(nums))                # 108
print(min(nums))                # 4
print(max(nums))                # 42
print(sorted(nums, reverse=True))   # [42, 23, 16, 15, 8, 4]   sorted() always returns a list

# list vs tuple vs set
# list  [ ]  ordered, allows duplicates, mutable      -> keep records in order
# tuple ( )  ordered, allows duplicates, immutable    -> fixed records, dict keys
# set   { }  unordered, unique items, mutable         -> de-duplication, membership, comparing groups

# empty set is False, non-empty set is True
print(bool(set()))              # False
print(bool({0}))                # True   it has one item, even if that item is 0
