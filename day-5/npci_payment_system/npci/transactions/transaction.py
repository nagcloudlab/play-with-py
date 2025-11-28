"""
Transaction class
"""

from datetime import datetime

class Transaction:
    """Represents a single payment transaction"""
    
    _counter = 10000
    
    def __init__(self, amount, sender_acc, receiver_acc, trans_type):
        Transaction._counter += 1
        self.txn_id = f"TXN{Transaction._counter}"
        self.amount = amount
        self.sender = sender_acc
        self.receiver = receiver_acc
        self.type = trans_type
        self.timestamp = datetime.now()
        self.status = "PENDING"
        self.failure_reason = None
    
    def mark_success(self):
        self.status = "SUCCESS"
    
    def mark_failed(self, reason):
        self.status = "FAILED"
        self.failure_reason = reason
    
    def __str__(self):
        time_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{self.txn_id}] {self.type}: ₹{self.amount:,} - {self.status} ({time_str})"