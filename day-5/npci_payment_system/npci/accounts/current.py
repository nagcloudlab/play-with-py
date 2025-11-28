"""
Current account implementation
"""

from .base import Account

class CurrentAccount(Account):
    """Current account with overdraft facility"""
    
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > (self._balance + self.overdraft_limit):
            print(f"✗ Exceeds overdraft limit of ₹{self.overdraft_limit}")
            return False
        
        self._balance -= amount
        return True
    
    def get_available_balance(self):
        """Get total available including overdraft"""
        return self._balance + self.overdraft_limit