"""
UPI payment gateway
"""

class UPIGateway:
    """Unified Payments Interface"""
    
    NAME = "UPI"
    TRANSACTION_LIMIT = 100000
    FEE_PERCENT = 0
    
    def __init__(self):
        self.transactions_processed = 0
    
    def validate(self, amount, sender):
        if amount <= 0:
            return False, "Invalid amount"
        if amount > self.TRANSACTION_LIMIT:
            return False, f"Exceeds UPI limit of ₹{self.TRANSACTION_LIMIT:,}"
        if sender.get_balance() < amount:
            return False, "Insufficient balance"
        return True, "Valid"
    
    def process(self, amount, sender, receiver):
        is_valid, msg = self.validate(amount, sender)
        if not is_valid:
            return False, msg
        
        sender.withdraw(amount)
        receiver.deposit(amount)
        self.transactions_processed += 1
        
        return True, f"UPI transfer of ₹{amount:,} successful"