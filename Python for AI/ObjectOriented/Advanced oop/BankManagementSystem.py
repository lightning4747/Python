class Transaction:
    def __init__(self, type, amount, balance_after):
        self.type = type
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = datetime.now()
    
    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M')} | {self.type:10} | ${self.amount:8.2f} | ${self.balance_after:8.2f}"

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self._balance = initial_balance
        self.transactions = []
        self._record_transaction("OPENING", initial_balance)
    
    def _record_transaction(self, type, amount):
        self.transactions.append(Transaction(type, amount, self._balance))
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._record_transaction("DEPOSIT", amount)
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._record_transaction("WITHDRAWAL", -amount)
            return True
        return False
    
    def get_balance(self):
        return self._balance
    
    def get_transaction_history(self):
        return self.transactions

# Test the system
from datetime import datetime

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
account.deposit(1000)

print(f"Balance: ${account.get_balance():.2f}")
print("\nTransaction History:")
print("Date       | Type       | Amount    | Balance")
print("-" * 50)
for transaction in account.get_transaction_history():
    print(transaction)