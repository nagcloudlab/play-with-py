import csv

def save_accounts_dict(accounts):
    """Save accounts using DictWriter (cleaner)"""
    
    fieldnames = ['account_number', 'holder_name', 'balance', 'account_type']
    
    with open("accounts_dict.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()  # Write header automatically
        writer.writerows(accounts)  # Write all rows
    
    print(f"✓ Saved {len(accounts)} accounts")


def read_accounts_dict():
    """Read accounts using DictReader (cleaner)"""
    
    with open("accounts_dict.csv", "r") as file:
        reader = csv.DictReader(file)
        
        accounts = []
        for row in reader:
            # row is already a dictionary!
            print(f"{row['account_number']}: {row['holder_name']} - ₹{float(row['balance']):,.2f}")
            accounts.append(row)
        
        return accounts


# Save
accounts = [
    {'account_number': 'ACC001', 'holder_name': 'Rajesh Kumar', 'balance': 50000, 'account_type': 'Savings'},
    {'account_number': 'ACC002', 'holder_name': 'Priya Sharma', 'balance': 75000, 'account_type': 'Current'},
]

save_accounts_dict(accounts)

# Read
print("\nReading accounts:")
loaded = read_accounts_dict()

# Output:
# ✓ Saved 2 accounts
# 
# Reading accounts:
# ACC001: Rajesh Kumar - ₹50,000.00
# ACC002: Priya Sharma - ₹75,000.00