"""
IMPS payment gateway
"""

class IMPSGateway:
    """Immediate Payment Service"""
    
    NAME = "IMPS"
    TRANSACTION_LIMIT = 200000
    FEE_PERCENT = 0.5
    
    def __init__(self):
        self.transactions_processed = 0
    
    def calculate_fee(self, amount):
        return amount * (self.FEE_PERCENT / 100)
    
    def validate(self, amount, sender):
        if amount <= 0:
            return False, "Invalid amount"
        if amount > self.TRANSACTION_LIMIT:
            return False, f"Exceeds IMPS limit of ₹{self.TRANSACTION_LIMIT:,}"
        
        fee = self.calculate_fee(amount)
        total = amount + fee
        
        if sender.get_balance() < total:
            return False, f"Insufficient balance (need ₹{total:,.2f} including fee)"
        return True, "Valid"
    
    def process(self, amount, sender, receiver):
        is_valid, msg = self.validate(amount, sender)
        if not is_valid:
            return False, msg
        
        fee = self.calculate_fee(amount)
        total = amount + fee
        
        sender.withdraw(total)
        receiver.deposit(amount)
        self.transactions_processed += 1
        
        return True, f"IMPS transfer of ₹{amount:,} successful (Fee: ₹{fee:.2f})"