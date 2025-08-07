# # Non Primitive Data Types.

# # list

# # Initializing a list with mixed data types
# L = [1, 2, True, "Abhi"]

# # 1. Append: Adds a single element at the end
# L.append("Bharath")  # Correct spelling

# # 2. Indexing: Accessing element at index 2
# print(L[2])  # Output: True

# # 3. Slicing: Accessing elements from index 1 to 2 (excludes index 3)
# print(L[1:3])  # Output: [2, True]

# # 4. Extend: Adds multiple elements to the list
# L.extend(["Biryani", "Chicken Sukka"])

# # 5. Insert: Adds element at a specific index
# L.insert(2, "I am at Second Index")

# # 6. Count: Counts how many times a specific object appears in the list
# print(L.count("Abhi"))  # Example usage, returns count of "Abhi"

# # 7. Remove: Removes the first occurrence of the specified value
# L.remove("Abhi")

# # 8. Pop: Removes element at the given index (or last if not specified)
# L.pop(3)  # Removes element at index 3

# # 9. Clear: Removes all elements but keeps the list object
# L.clear()

# # 10. Sort: Sorts the list (only if the elements are of same type like all numbers or all strings)
# # Example:
# numbers = [5, 2, 9, 1]
# numbers.sort()  # Ascending order
# print(numbers)

# # Sort in descending order
# numbers.sort(reverse=True)
# print(numbers)

# # Sort using a key (e.g., string length)
# names = ["Ram", "Krishna", "Om"]
# sorted_names = sorted(names, key=len)
# print(sorted_names)

#  ******list sorting and filter practice in lists having mixed data types*****

l=[1,"two",3.0,"four",4,9]

# extarcting related data types and sorting
ints=sorted(x for x in l if isinstance(x,int))
strings=sorted(x for x in l if isinstance(x,str),key=len)
print(ints)
print(strings)
  
#  sorting based on position of the character
data = [("a", 3), ("b", 1), ("c", 2)]
sorted_data = sorted(data, key=lambda x: x[0])
print(sorted_data)  # [('b', 1), ('c', 2), ('a', 3)]

