# How to Print in Python

print("Hello World")
print("Tday I am starting Python")

print("Hi My name is Abhi")
print (7)
print(7.8)

print("hello",1,1.6,True,sep="/")
print("hello",1,1.6,True,sep="*")

a = "Abhi"
b = "Shravana"
print(a+" "+b)

num = 1234.12234
print(f"the number is {num:.2f}")

print("line_1\nline_2\nline_3")

print("""hello
my name is abhi
I am learning python because i want to become 
top software engineers in the worls""")

# without using the f-string
print("my name is",a, "my age is ",num)

#using the format method
print("My name is {}, My age is {}".format(a,b))

#using the fstring
print(f"hello my name is {b}")

#defineing the variables 
u_name = "abhi"
l_name = 'gowda'
u_age = 25
u_active = True

# we using the "," for put commas as thousand separator 
l_num = 98765342.22
print(f'{l_num:,.1f}') # 98,765,342.2

#the "sep" cant be used in the f'string 
print(f"{u_name},{l_name},{u_age},sep='|'") 

#the "sep" will work here in where we are passing seprate values to print
print(u_name,l_name,u_age,sep="|") 

# "f" is the specify and it hold up to 6 decimal points by default 

x = 4.56789456
print(f"{x:f}") # It will round of to the 6 values like "4.567895" and the 5&6 is lost 

y = 5.6783
print(f"{y:f}") # It will pads another 2 zeros to the y object,because by default it will holds the 6 values after the '.' decimal

z = 45.7896
print(f"{z:.2f}") # we are specifying round off "2" is the round of decimal here so "45.79"

a = 12345678
print(f"{a:,}")        # gives 12,345,678 because its an interger plain {a:,} is enof

# % is a type, like f. It multiplies by 100 and adds the % sign.
print(f"{0.18:%}")     # 18.000000%    default 6 decimals, same rule as f
print(f"{0.18:.0%}")   # 18%
print(f"{0.1834:.1%}") # 18.3%

# zero-padding , if we have decimal we need to count it as and digit value
print(f"{12345:05d}")   # 12345    (already 5 digits, no padding)
print(f"{7:05d}")       # 00007    (1 digit, so 4 zeros are added)
print(f"{123:05d}")     # 00123    (3 digits, so 2 zeros are added)
print(f"{3.14159:07.3f}") #003.142  (the decimal is roundoff for 3 points and we include the '.' also then total we have 5 value we padd another 2 zeros)