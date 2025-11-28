import json

def read_account_json():
    """Read account from JSON file"""
    
    with open("account.json", "r") as file:
        account = json.load(file)  # Parse JSON to Python dict
    
    print("Account Information:")
    print(f"  Account Number: {account['account_number']}")
    print(f"  Holder: {account['holder']['name']}")
    print(f"  Email: {account['holder']['email']}")
    print(f"  Balance: ₹{account['balance']:,.2f}")
    print(f"  Type: {account['account_type']}")
    
    print(f"\n  Address:")
    addr = account['holder']['address']
    print(f"    {addr['street']}")
    print(f"    {addr['city']}, {addr['state']} - {addr['pincode']}")
    
    print(f"\n  Recent Transactions:")
    for txn in account['transactions']:
        print(f"    {txn['id']}: {txn['type']} ₹{txn['amount']:,.2f} on {txn['date']}")
    
    print(f"\n  Settings:")
    settings = account['settings']
    print(f"    SMS Alerts: {'Enabled' if settings['sms_alerts'] else 'Disabled'}")
    print(f"    Email Alerts: {'Enabled' if settings['email_alerts'] else 'Disabled'}")
    print(f"    Daily Limit: ₹{settings['daily_limit']:,.2f}")
    
    return account


account = read_account_json()

# Output:
# Account Information:
#   Account Number: ACC001
#   Holder: Rajesh Kumar
#   Email: rajesh@example.com
#   Balance: ₹50,000.00
#   Type: Savings
# 
#   Address:
#     123 MG Road
#     Mumbai, Maharashtra - 400001
# 
#   Recent Transactions:
#     TXN001: CREDIT ₹5,000.00 on 2024-01-10
#     TXN002: DEBIT ₹2,000.00 on 2024-01-12
#     TXN003: CREDIT ₹3,000.00 on 2024-01-14
# 
#   Settings:
#     SMS Alerts: Enabled
#     Email Alerts: Enabled
#     Daily Limit: ₹50,000.00