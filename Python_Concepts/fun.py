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

