# # Non Primitive Data Types.

''' lists
    mutable
    indexable'''

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

# **list sorting and filter practice in lists having mixed data types**

# l=[1,"two",3.0,"four",4,9]

# # extarcting related data types and sorting
# ints = sorted(x for x in l if isinstance(x, int))
# strings = sorted((x for x in l if isinstance(x, str)), key=len)
# final_list = ints + strings
# print(ints)
# print(strings)

  
# #  sorting based on position of the character
# data = [("a", 3), ("b", 1), ("c", 2)]
# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)  # [('b', 1), ('c', 2), ('a', 3)]


'''  tuples methods
    1.tuples are immutable
    2.ordered and indexable  '''

# syntax
tuple=(1,2,3,"cat",5.0,3,3)

# accesing elememnts by indexing
print(tuple[3])

# accesing elements by slicing
print(tuple[3:0:-1])  #slicing syntax[start_index, end_index, step_size], step size=-1 for accessing in reverse order ,by default it 1 ie in forward order.

# built in methods available
# count methods to count number of times a given elements is preent in the tuple
print(tuple.count(3))

# index method return the index of the given element in the tuple
print(tuple.index(3))   # returns first occurence index in case if element is present mutiple times in the tuple

# pure tuples are immutable.,if the tuple contains other data type nested inside it can be mutable(can be updated)
tuple_1=(1,2,3,[7,8],{'a','b','c'})
tuple_1[3][1]=9
print(tuple_1)   #replces elemt in list at index 1


''' dictionaries
  1.stores data in key values format
  2.keys are used for accesing values 
  3.keys should be unique 
  4.mutable 
  5.Keys must be unique
  6.Keys must be immutable (str, int, tuple, etc.)
  7.Values can be anything: list, dict, etc.'''

                         
dict={'a':1,'b':2,'name':'yogesh'}

# accessing through keys
print(dict['a'])
print(dict.get('name'))  #usingget method

# commonly used methods on dictionary
print('name' in dict)   #to check if key is presnt in the dictionary


# to print all the keys present in the dictionary
print(dict.keys())   

# to print all the values in the dictionary
print(dict.values())

# to print all the items ie keys and values present in the dictionary
print(dict.items())

# changing the values
dict['a']=100
print(dict.values())


# update method- used to more key values pairs inside dictionary or to override the values persent in the keys 

print(dict.update({'a':500,"c":"laptop",5.0:[4,5,6]}))


print(dict.items())







