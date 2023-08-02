# define the class savingsAccount
class savingsAccount:
    # define the class constructor
    def __init__(self, name, balance):
        # define the class attributes
        self.name = name
        self.balance = balance
#  create the methods of the class - deposit, withdraw, calculate interest and check balance
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def calculateInterest(self, rate):
        self.balance += self.balance * rate

    def checkBalance(self):
        return self.balance
# define the __str__ method to print the object - this is the DUnder method that allows overloading in Python
    def __str__(self):
        return "Name: " + self.name + "\nBalance: " + str(self.balance)

print("Welcome to the savings account program")
# create the object and declare a variable to reference that specific object
account = savingsAccount("Belinda", 25000)
# print the object
print(account)
# deposit 500
account.deposit(500)
# print the object
print(account)
# withdraw 2000
account.withdraw(2000)
# print the object
print(account)
# withdraw 500
account.withdraw(500)
# print the object
print(account)
# calculate interest at 5%
account.calculateInterest(0.05)
# print the object
print(account)