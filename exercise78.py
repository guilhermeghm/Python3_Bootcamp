#My solution
# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, number):
        self.balance = self.balance + number
        return self.balance

    def withdraw(self, number):
        self.balance = self.balance - number
        return self.balance

#Official solution
class BankAccount:

    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
