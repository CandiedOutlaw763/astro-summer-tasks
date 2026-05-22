from datetime import datetime

class Account:
    def __init__(self, balance=0):
        self.name = input("Name of account holder: ")
        self.number = input("Account Number: ")
        self.pwd = input("Enter Password: ")
        self.balance = balance
        self.t = {}
    
    def deposit(self, amount):
        self.check()
        self.balance = self.balance + amount
        self.t[datetime.now().strftime("%Y-%m-%d %H:%M:%S")] = "+"+str(amount)
    
    def withdraw(self, amount):
        self.check()
        if amount < self.balance:
            self.balance = self.balance - amount
            self.t[datetime.now().strftime("%Y-%m-%d %H:%M:%S")] = "-"+str(amount)
        else:
            print("Insufficient balance")

    def bal(self):
        self.check()
        print(self.balance)

    def details(self):
        self.check()
        print("Name of account holder: " + str(self.name))
        print("Account number: " + str(self.number))
        print(self.t)

    def check(self):
        while True:
            pw = input("Please enter password: ")
            if self.pwd == pw:
                break
            else:
                print("Incorrect password. Please try again.\n")



accounts = []

def search():
    num = input("Enter your account number: ")

    for i in accounts:
        if i.number == num:
            return i
    return None
print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Display Account Details\n6. Exit")
while True:
    a = input("What would you like to do? ")

    if a == "1":
        accounts.append(Account())
    elif a == "2":
        b = search()
        if b != None:
            am = int(input("Enter amount to deposit: "))
            b.deposit(am)
        else:
            print("Account not found.")
    elif a == "3":
        b = search()
        if b != None:
            am = int(input("Enter amount to withdraw: "))
            b.withdraw(am)
        else:
            print("Account not found.")
    elif a == "4":
        b = search()
        if b != None:
            b.bal()
        else:
            print("Account not found.")
    elif a == "5":
        b = search()
        if b != None:
            b.details()
        else:
            print("Account not found.")
    elif a == "6":
        print("Thank you for using our services.")
        break
        