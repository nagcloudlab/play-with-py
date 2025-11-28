"""
Transaction history management
"""

class TransactionHistory:
    """Maintains transaction records"""
    
    def __init__(self):
        self.transactions = []
    
    def add(self, transaction):
        self.transactions.append(transaction)
    
    def get_recent(self, count=10):
        return self.transactions[-count:]
    
    def get_successful(self):
        return [t for t in self.transactions if t.status == "SUCCESS"]
    
    def get_failed(self):
        return [t for t in self.transactions if t.status == "FAILED"]
    
    def get_total_volume(self):
        return sum(t.amount for t in self.get_successful())
    
    def get_by_type(self, trans_type):
        return [t for t in self.transactions if t.type == trans_type]