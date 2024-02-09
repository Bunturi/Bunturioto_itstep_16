# Homework N16.1
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

# deposit
    def deposit(self, amount):
        self.balance += amount
        print(f"Dear {self.account_holder}, deposited {amount} into account "
              f"{self.account_number}. New balance: {self.balance} Gel")

# withdraw
    def withdraw(self, amount):
        # check balance if there are enough amount
        if self.balance > amount:
            self.balance -= amount
            print(f"Dear {self.account_holder}, withdrew {amount} from account "
                  f"{self.account_number}. New balance: {self.balance} Gel")
        else:
            print(f"Dear {self.account_holder}, there are insufficient funds in account "
                  f"{self.account_number} to withdraw {amount} Gel")
