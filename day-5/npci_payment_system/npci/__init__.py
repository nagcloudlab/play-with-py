"""
NPCI Payment System Package

A comprehensive payment processing system supporting UPI, IMPS, and NEFT.
"""

__version__ = "1.0.0"
__author__ = "NPCI Development Team"

# Import main components for easy access
from .accounts import Account, SavingsAccount, CurrentAccount
from .payments import UPIGateway, IMPSGateway, NEFTGateway, get_gateway
from .transactions import Transaction, TransactionHistory
from . import utils

# Package-level configuration
DEFAULT_CURRENCY = "INR"
DEFAULT_GATEWAY = "UPI"

print(f"NPCI Payment System v{__version__} initialized")