"""
NEFT payment gateway
"""

class NEFTGateway:
    """National Electronic Funds Transfer"""
    
    NAME = "NEFT"
    FEE_PERCENT = 0.2
    
    def __init__(self):
        self.transactions_processed = 0
    
    def calculate_fee(self, amount):
        fee = amount * (self.FEE_PERCENT / 100)
        # NEFT has minimum and maximum fees
        return max(2.5, min(fee, 25))
    
    def validate(self, amount, sender):
        if amount <= 0:
            return False, "Invalid amount"
        
        fee = self.calculate_fee(amount)
        total = amount + fee
        
        if sender.get_balance() < total:
            return False, f"Insufficient balance"
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
        
        return True, f"NEFT transfer of ₹{amount:,} successful (Fee: ₹{fee:.2f}, settles in batch)"