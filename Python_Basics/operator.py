# operators in python - symbols that perform an operation on the values (operands)

a = 17
b = 5

# arithmetic operators - + , - , * , / , // , % , **

print(a + b)        # 22      addition
print(a - b)        # 12      subtraction
print(a * b)        # 85      multiplication
print(a / b)        # 3.4     division, always gives a float
print(a // b)       # 3       floor division, drops the decimal part
print(a % b)        # 2       modulus, the remainder
print(a ** b)       # 1419857 power, 17 to the power 5

print(10 / 2)       # 5.0     still a float, even though it's a whole number
print(-17 // 5)     # -4      floor goes DOWN to the lower number, not towards zero
print(-17 % 5)      # 3       the result takes the sign of the right operand

# + and * also work on the strings
print("abhi" + "gowda")     # abhigowda
print("ab" * 3)             # ababab

# comparison operators - ==, !=, >, <, >=, <= , the result is always a bool

print(a == b)       # False
print(a != b)       # True
print(a > b)        # True
print(a < b)        # False
print(a >= 17)      # True
print(a <= 16)      # False

print(5 == 5.0)     # True    compares the value, not the type
print("a" < "b")    # True    strings are compared alphabetically

# "=" assigns the value and "==" compares the value, don't mix them up

# chained comparison
age = 25
print(18 <= age <= 60)      # True    same as (18 <= age) and (age <= 60)

# assignment operators - = , += , -= , *= , /= , //= , %= , **=

x = 10
x += 5          # x = x + 5
print(x)        # 15
x -= 3          # x = x - 3
print(x)        # 12
x *= 2          # x = x * 2
print(x)        # 24
x /= 4          # x = x / 4
print(x)        # 6.0  (/ makes it a float)
x //= 4         # x = x // 4
print(x)        # 1.0
x = 7
x %= 3          # x = x % 3
print(x)        # 1
x **= 3         # x = x ** 3
print(x)        # 1

# logical operators - and , or , not

is_active = True
in_stock = False

print(is_active and in_stock)       # False   both must be True
print(is_active or in_stock)        # True    at least one must be True
print(not is_active)                # False   flips the value

# short-circuit - python stops as soon as the answer is known
print(0 and 5)          # 0       "and" returns the first falsy value, else the last value
print(3 and 5)          # 5
print(0 or 5)           # 5       "or" returns the first truthy value, else the last value
print("" or "default")  # default  handy for fallback values

# identity operators - is , is not , checks whether both are the SAME object in memory

supplier = None
print(supplier is None)         # True    the right way to check for None
print(supplier is not None)     # False

p = [1, 2]
q = [1, 2]
r = p
print(p == q)       # True    same values
print(p is q)       # False   different objects in memory
print(p is r)       # True    r points to the same object as p

# membership operators - in , not in , checks if a value is present in a sequence

teams = ['CSK', 'MI', 'BNG']

print('CSK' in teams)           # True
print('RCB' in teams)           # False
print('RCB' not in teams)       # True
print('bhi' in "abhi")          # True    works on the strings too (substring)

# bitwise operators - &, |, ^, ~, <<, >>  , they work on the binary bits of the int

m = 6           # 0110
n = 3           # 0011

print(m & n)    # 2     0010  AND, 1 only if both bits are 1
print(m | n)    # 7     0111  OR, 1 if any bit is 1
print(m ^ n)    # 5     0101  XOR, 1 if the bits are different
print(~m)       # -7    NOT, flips the bits, gives -(m + 1)
print(m << 1)   # 12    shift left by 1, same as m * 2
print(m >> 1)   # 3     shift right by 1, same as m // 2

# operator precedence - which one runs first (high to low)
# ** , then unary (+x, -x, ~x) , then * / // % , then + - , then comparisons , then not , and , or

print(2 + 3 * 4)        # 14    * runs before +
print((2 + 3) * 4)      # 20    brackets change the order
print(2 ** 3 ** 2)      # 512   ** goes right to left, 2 ** (3 ** 2)
print(-2 ** 2)          # -4    ** runs before the minus, -(2 ** 2)
print(True or False and False)  # True   "and" runs before "or"

# walrus operator - := assigns a value and uses it in the same expression
if (length := len("abhishek")) > 5:
    print(length)       # 8
