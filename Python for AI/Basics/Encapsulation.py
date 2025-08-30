import numpy

class Bank:
    def __init__(self, balance: int, pin: int, accountnumber: int):
        self.__balance = balance
        self.__pin = pin
        self.accountnumber = accountnumber

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.__balance += amount
            print(f"{amount}$ has been successfully credited.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: int, pin: int) -> None:
        if pin != self.__pin:
            print("Invalid PIN.")
            return
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient balance.")
            return

        self.__balance -= amount
        print(f"{amount}$ has been withdrawn successfully.")

    def get_balance(self) -> int:
        return self.__balance  

    def __str__(self) -> str:
        return f"Account {self.accountnumber} | Balance: {self.__balance}$"


# -------------------------------
# Usage
# -------------------------------
b1 = Bank(1000, 1234, 123456789)

print(b1)                     # Calls __str__
b1.deposit(100)
b1.withdraw(1000, 1234)
print(f"Final Balance: {b1.get_balance()}$")
