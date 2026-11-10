# Encapsulation in Python

class BankAccount:

    def __init__(self,name,balance):
        self.Name = name
        self._BankName = "SBI"
        self.__balance = balance
    
    def BankName(self):
        Updated_BankName = input("Enter the Bank Name: ")
        self._BankName = Updated_BankName
        print(f"Your Bank Name is, {self._BankName}.")

    def get_Balance(self):
        bal = self.__balance
        print(f"Your Account Balance is, {bal}.")
    
    def set_Deposit(self):
        try:
            amount = float(input("Enter the Amount: "))
            if amount < 0:
                print("Invalid Amount")
            else:
                self.__balance += amount
                print(f"Amount has been deposited: {amount}")
        except ValueError:
            print("Please enter a valid number.")
        finally:
            print("Transaction Completed, Have a Good Day.....")
      
    def Withdraw_Amount(self,Withdraw_amt):
        if Withdraw_amt > self.__balance :
            print("Dont Have Sufficient Balance.")
        else:
            self.__balance -= Withdraw_amt
            print(f"Your WithDrawal Amount is, {Withdraw_amt} and Remaing Account Balance is,{self.__balance}")

    def get_UserDetails(self):
        print(f"Account Holder Name : {self.Name}.")
        print(f"Bank Name : {self._BankName}.")
        print(f"Account Balance : {self.__balance}")


User_One = BankAccount("Abhishek",5000)

User_One.get_UserDetails()

User_One.Withdraw_Amount(2000)

User_One.get_Balance()

User_One.set_Deposit()

User_One.BankName()

# Getter is Used to Read the Private Varible Value.

# Setter is Used to Update Private Varible Safely(With Validation).

# Yes, We can Change the Protect Varible Value ,
# But But the convention tells developers: "Don't modify me unless you're in a subclass."

# Yes ,We can Access the Value of Private alo by this but ,So technically it's possible, but discouraged.
#  Private variables enforce data hiding.

print(User_One._BankAccount__balance)