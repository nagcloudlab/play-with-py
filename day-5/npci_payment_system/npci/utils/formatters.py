"""
Formatting utilities
"""

import random
import string

def format_currency(amount):
    """Format amount in Indian rupee style"""
    return f"₹{amount:,.2f}"

def format_account_number(account_number):
    """Format account number with spaces"""
    # HDFC1234567890 -> HDFC 1234 5678 90
    if len(account_number) > 4:
        prefix = account_number[:4]
        rest = account_number[4:]
        groups = [rest[i:i+4] for i in range(0, len(rest), 4)]
        return f"{prefix} {' '.join(groups)}"
    return account_number

def generate_account_number(prefix="ACC"):
    """Generate random account number"""
    digits = ''.join(random.choices(string.digits, k=10))
    return f"{prefix}{digits}"

def generate_transaction_id():
    """Generate unique transaction ID"""
    import time
    timestamp = str(int(time.time()))
    random_part = ''.join(random.choices(string.digits, k=4))
    return f"TXN{timestamp}{random_part}"