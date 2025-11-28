"""
Validation utilities
"""

import re

def validate_account_number(account_number):
    """Validate account number format"""
    return bool(re.match(r'^[A-Z]{3}\d{6,12}$', account_number))

def validate_upi_id(upi_id):
    """Validate UPI ID format"""
    pattern = r'^[\w.-]+@[\w.-]+$'
    return bool(re.match(pattern, upi_id))

def validate_ifsc(ifsc_code):
    """Validate IFSC code"""
    pattern = r'^[A-Z]{4}0[A-Z0-9]{6}$'
    return bool(re.match(pattern, ifsc_code))

def validate_mobile(mobile):
    """Validate Indian mobile number"""
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, mobile))