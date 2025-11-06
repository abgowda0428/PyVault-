def add(a,b):
    return a+b

c = add(1,8)
print(c)

# Python Function

def Cal_Discount(Orginal_Price,Discounted_Price):
    Dis_spilt = int(Discounted_Price[:-1])
    return (Orginal_Price / 100) * Dis_spilt

Dis_amount = Cal_Discount(10000,"25%")
print(Dis_amount)

# Lambda Function

n = int(input("Enter the Number ?"))

Is_Even = lambda n : print("Even") if n % 2 == 0 else print("Odd")
Is_Even(n)


# **kwrags

Is_Even_Kw = lambda **kwargs: {k: ("Even" if v % 2 == 0 else "Odd") for k, v in kwargs.items()}

print(Is_Even_Kw(a=2, b=5, c=8))
# Output: {'a': 'Even', 'b': 'Odd', 'c': 'Even'}

# *args
Is_All_Even = lambda *args: all(n % 2 == 0 for n in args) #all() is a built-in function.
                                                          #It returns True if all elements in an iterable are True.
                                                          #Returns False if any one element is False.

print(Is_All_Even(2, 4, 6))   # True
print(Is_All_Even(2, 3, 6))   # False

# Two Parameter
Is_Divisible = lambda x, y: print(f"{x} is divisible by {y}") if x % y == 0 else print(f"{x} is not divisible by {y}")

Is_Divisible(10, 2)  # ✅ "10 is divisible by 2"
Is_Divisible(7, 3)   # ✅ "7 is not divisible by 3"


