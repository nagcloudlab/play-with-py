import csv

def read_accounts_csv():
    """Read accounts from CSV file"""
    
    accounts = []
    
    with open("accounts.csv", "r") as file:
        reader = csv.reader(file)
        
        # Skip header
        header = next(reader)
        print(f"Headers: {header}\n")
        
        # Read data rows
        for row in reader:
            account = {
                'number': row[0],
                'name': row[1],
                'balance': float(row[2]),
                'type': row[3]
            }
            accounts.append(account)
            print(f"{account['number']}: {account['name']} - ₹{account['balance']:,.2f} ({account['type']})")
    
    return accounts


accounts = read_accounts_csv()
print(f"\n✓ Loaded {len(accounts)} accounts")

# Output:
# Headers: ['Account Number', 'Holder Name', 'Balance', 'Type']
# 
# ACC001: Rajesh Kumar - ₹50,000.00 (Savings)
# ACC002: Priya Sharma - ₹75,000.00 (Current)
# ACC003: Amit Patel - ₹30,000.00 (Savings)
# ACC004: Sneha Gupta - ₹100,000.00 (Current)
# 
# ✓ Loaded 4 accounts