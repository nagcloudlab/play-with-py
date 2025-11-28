import sqlite3

conn = sqlite3.connect('npci_bank.db')
cursor = conn.cursor()

# Get top 3 accounts by balance
print("Top 3 Accounts by Balance:")
cursor.execute("""
    SELECT account_number, holder_name, balance 
    FROM accounts 
    ORDER BY balance DESC 
    LIMIT 3
""")

for i, account in enumerate(cursor.fetchall(), 1):
    print(f"  {i}. {account[1]}: ₹{account[2]:,.2f}")

# Get all accounts sorted by name
print("\nAccounts (Sorted by Name):")
cursor.execute("""
    SELECT account_number, holder_name, balance 
    FROM accounts 
    ORDER BY holder_name ASC
""")

for account in cursor.fetchall():
    print(f"  {account[1]} ({account[0]}): ₹{account[2]:,.2f}")

conn.close()

# Output:
# Top 3 Accounts by Balance:
#   1. Sneha Gupta: ₹100,000.00
#   2. Priya Sharma: ₹75,000.00
#   3. Rajesh Kumar: ₹50,000.00
#
# Accounts (Sorted by Name):
#   Amit Patel (ACC003): ₹30,000.00
#   Priya Sharma (ACC002): ₹75,000.00
#   Rajesh Kumar (ACC001): ₹50,000.00
#   Sneha Gupta (ACC004): ₹100,000.00