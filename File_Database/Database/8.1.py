import sqlite3

conn = sqlite3.connect('npci_bank.db')
cursor = conn.cursor()

# Select all accounts
cursor.execute("SELECT * FROM accounts")
accounts = cursor.fetchall() # list of tuples

print("All Accounts:")
print("-" * 70)
for account in accounts:
    acc_num, holder, balance, acc_type, created = account
    print(f"{acc_num}: {holder} - ₹{balance:,.2f} ({acc_type})")

conn.close()

# Output:
# All Accounts:
# ----------------------------------------------------------------------
# ACC001: Rajesh Kumar - ₹50,000.00 (Savings)
# ACC002: Priya Sharma - ₹75,000.00 (Current)
# ACC003: Amit Patel - ₹30,000.00 (Savings)
# ACC004: Sneha Gupta - ₹100,000.00 (Current)