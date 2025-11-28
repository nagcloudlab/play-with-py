import json

def save_multiple_accounts():
    """Save multiple accounts to JSON"""
    
    accounts = [
        {
            "account_number": "ACC001",
            "holder_name": "Rajesh Kumar",
            "balance": 50000,
            "type": "Savings"
        },
        {
            "account_number": "ACC002",
            "holder_name": "Priya Sharma",
            "balance": 75000,
            "type": "Current"
        },
        {
            "account_number": "ACC003",
            "holder_name": "Amit Patel",
            "balance": 30000,
            "type": "Savings"
        }
    ]
    
    with open("all_accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)
    
    print(f"✓ Saved {len(accounts)} accounts")


def search_account(account_number):
    """Search for specific account"""
    
    with open("all_accounts.json", "r") as file:
        accounts = json.load(file)
    
    for account in accounts:
        if account['account_number'] == account_number:
            print(f"\nAccount Found:")
            print(f"  Number: {account['account_number']}")
            print(f"  Holder: {account['holder_name']}")
            print(f"  Balance: ₹{account['balance']:,.2f}")
            print(f"  Type: {account['type']}")
            return account
    
    print(f"\n✗ Account {account_number} not found")
    return None


def update_balance(account_number, new_balance):
    """Update account balance in JSON file"""
    
    with open("all_accounts.json", "r") as file:
        accounts = json.load(file)
    
    # Find and update account
    found = False
    for account in accounts:
        if account['account_number'] == account_number:
            old_balance = account['balance']
            account['balance'] = new_balance
            found = True
            print(f"✓ Updated {account_number}: ₹{old_balance:,.2f} → ₹{new_balance:,.2f}")
            break
    
    if not found:
        print(f"✗ Account {account_number} not found")
        return False
    
    # Save back to file
    with open("all_accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)
    
    return True


# Demo
save_multiple_accounts()

# Search
search_account("ACC002")

# Update
update_balance("ACC002", 80000)

# Verify
search_account("ACC002")

# Output:
# ✓ Saved 3 accounts
# 
# Account Found:
#   Number: ACC002
#   Holder: Priya Sharma
#   Balance: ₹75,000.00
#   Type: Current
# 
# ✓ Updated ACC002: ₹75,000.00 → ₹80,000.00
# 
# Account Found:
#   Number: ACC002
#   Holder: Priya Sharma
#   Balance: ₹80,000.00
#   Type: Current