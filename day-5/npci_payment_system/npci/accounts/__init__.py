
"""
Accounts package - manages all account types
"""

from .base import Account
from .savings import SavingsAccount
from .current import CurrentAccount

# Package version
__version__ = "1.0.0"

# Expose main classes at package level
__all__ = ['Account', 'SavingsAccount', 'CurrentAccount']

print(f"Accounts package v{__version__} loaded")