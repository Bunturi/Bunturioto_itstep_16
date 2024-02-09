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


# Creating accounts
account_1 = BankAccount("123456", "Oto",500)
account_2 = BankAccount("789012", "Anna", 1000)

# Transactions
account_1.deposit(500)
account_1.withdraw(150)

account_2.withdraw(200)
account_2.withdraw(1500)  # Withdraw more than balance


#Homework N16.2
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    # Show student info
    def student_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Courses Enrolled: {', '.join([course for course in self.courses])}")

    # Append chosen courses
    def chosen_courses(self, course):
        self.courses.append(course)


# Creating students
student_1 = Student("Oto", "st-0001")
student_2 = Student("Tamo", "st-0002")

# Courses
student_1.chosen_courses("Mathematics")
student_1.chosen_courses("Physics")

student_2.chosen_courses("History")
student_2.chosen_courses("Philosophy")

# Displaying student information
student_1.student_info()
print("\n")
student_2.student_info()
