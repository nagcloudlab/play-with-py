"""
Base account class
"""

class Account:
    """Base class for all account types"""
    
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self._balance
    
    def __str__(self):
        return f"{self.holder_name} ({self.account_number}): ₹{self._balance:,.2f}"