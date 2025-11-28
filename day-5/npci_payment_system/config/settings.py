"""
Configuration settings for NPCI system
"""

# Database settings (for future use)
DATABASE = {
    'host': 'localhost',
    'port': 5432,
    'name': 'npci_db'
}

# Payment limits
PAYMENT_LIMITS = {
    'UPI': 100000,
    'IMPS': 200000,
    'NEFT': 1000000
}

# Fee structure
FEE_STRUCTURE = {
    'UPI': 0,
    'IMPS': 0.5,
    'NEFT': 0.2
}

# Account settings
ACCOUNT_SETTINGS = {
    'savings': {
        'min_balance': 1000,
        'daily_limit': 50000,
        'interest_rate': 4.0
    },
    'current': {
        'min_balance': 5000,
        'overdraft_default': 50000
    }
}