"""
Savings account implementation
"""

from .base import Account

class SavingsAccount(Account):
    """Savings account with interest and daily limit"""
    
    DAILY_LIMIT = 50000
    INTEREST_RATE = 4.0  # Annual interest rate %
    
    def __init__(self, account_number, holder_name, balance):
        super().__init__(account_number, holder_name, balance)
        self.daily_withdrawn = 0
    
    def withdraw(self, amount):
        if self.daily_withdrawn + amount > self.DAILY_LIMIT:
            print(f"✗ Daily limit of ₹{self.DAILY_LIMIT} exceeded")
            return False
        
        if super().withdraw(amount):
            self.daily_withdrawn += amount
            return True
        return False
    
    def reset_daily_limit(self):
        """Reset daily withdrawal counter"""
        self.daily_withdrawn = 0
    
    def calculate_interest(self):
        """Calculate monthly interest"""
        monthly_rate = self.INTEREST_RATE / 12 / 100
        interest = self._balance * monthly_rate
        return interest