import csv

def save_accounts_csv(accounts):
    """Save multiple accounts to CSV file"""
    
    with open("accounts.csv", "w", newline='') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(["Account Number", "Holder Name", "Balance", "Type"])
        
        # Write data rows
        for acc in accounts:
            writer.writerow([acc['number'], acc['name'], acc['balance'], acc['type']])
    
    print(f"✓ Saved {len(accounts)} accounts to CSV")


# Sample data
accounts = [
    {'number': 'ACC001', 'name': 'Rajesh Kumar', 'balance': 50000, 'type': 'Savings'},
    {'number': 'ACC002', 'name': 'Priya Sharma', 'balance': 75000, 'type': 'Current'},
    {'number': 'ACC003', 'name': 'Amit Patel', 'balance': 30000, 'type': 'Savings'},
    {'number': 'ACC004', 'name': 'Sneha Gupta', 'balance': 100000, 'type': 'Current'},
]

save_accounts_csv(accounts)

# Output:
# ✓ Saved 4 accounts to CSV

# View file contents:
# Account Number,Holder Name,Balance,Type
# ACC001,Rajesh Kumar,50000,Savings
# ACC002,Priya Sharma,75000,Current
# ACC003,Amit Patel,30000,Savings
# ACC004,Sneha Gupta,100000,Current