# Class → Blueprint to create objects
# Object → Instance of a class
# Encapsulation → Hiding data using private variables
# Abstraction → Showing only required details
# Inheritance → Reusing properties from another class
# Polymorphism → Same function, different behavior

# ================================
# OOPs Example: Bank Account System
# ================================

# 🔹 Class (Blueprint)
class Account:
    def __init__(self, name, balance):
        # 🔹 Encapsulation (private variable using __)
        self.name = name
        self.__balance = balance   # private variable

    # 🔹 Getter method (Abstraction → controlled access)
    def get_balance(self):
        return self.__balance

    # 🔹 Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid amount")

    # 🔹 Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully")
        else:
            print("Insufficient balance")

    # 🔹 Method to display info
    def show(self):
        print(f"Account Holder: {self.name}, Balance: {self.__balance}")


# 🔹 Inheritance (SavingAccount inherits Account)
class SavingAccount(Account):
    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self.interest = interest

    # 🔹 Polymorphism (same method name, different behavior)
    def show(self):
        print(f"[Savings] {self.name} | Balance: {self.get_balance()} | Interest: {self.interest}%")


# 🔹 Another child class
class CurrentAccount(Account):
    def __init__(self, name, balance, overdraft):
        super().__init__(name, balance)
        self.overdraft = overdraft

    # 🔹 Polymorphism
    def show(self):
        print(f"[Current] {self.name} | Balance: {self.get_balance()} | Overdraft: {self.overdraft}")


# ================================
# 🔹 Object Creation
# ================================

acc1 = SavingAccount("Prateek", 1000, 5)
acc2 = CurrentAccount("Ravi", 2000, 500)

# ================================
# 🔹 Operations
# ================================

acc1.deposit(500)
acc1.withdraw(200)
acc1.show()

print("------")

acc2.withdraw(2500)  # overdraft case (still using parent logic)
acc2.show()

# ================================
# 🔹 Encapsulation Test
# ================================

# ❌ This will NOT work (private variable)
# print(acc1.__balance)

# ✅ Correct way
print("Balance using getter:", acc1.get_balance())