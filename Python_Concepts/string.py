# string accesing value
y = "lion"
print(y[3])

# string slicing
x = "abhishek"
print(x[0:3])

print(x.upper())
print(y.replace("on","ld"))

a = "tagruu,sheep"
print(a.split(","))

numbers = [10, 20, 30, 40]

for i in range(10,20):
    print(i)

print("Break")

for i in numbers:
    print(i)

names = ["Abhishek", "Rahul", "Priya", "Sneha", "Kiran","Pig"]

for name in names:
    if(name == "Pig"):
        print("My Love")
        print(name)
        break
    print(name)    

for name in names:
    if(name == "Pig"):
        print("My Love")
        continue
    print(name)    

d = {"Abhi" : 123, "sanday" : 456}
print(type(d))

e = [1,"a",2,True]
print(type(e))

f = (1,2,3,3,4,5,5)
print(type(f))

