import sqlite3

conn = sqlite3.connect('npci_bank.db')
cursor = conn.cursor()

# Find specific account
cursor.execute(
    "SELECT * FROM accounts WHERE account_number = ?",
    ("ACC001",)
)
account = cursor.fetchone()

if account:
    acc_num, holder, balance, acc_type, created = account
    print(f"Account Found:")
    print(f"  Number: {acc_num}")
    print(f"  Holder: {holder}")
    print(f"  Balance: ₹{balance:,.2f}")
    print(f"  Type: {acc_type}")
else:
    print("Account not found")

# Find all Savings accounts
print("\nSavings Accounts:")
cursor.execute(
    "SELECT * FROM accounts WHERE account_type = ?",
    ("Savings",)
)
savings_accounts = cursor.fetchall()

for account in savings_accounts:
    print(f"  {account[0]}: {account[1]} - ₹{account[2]:,.2f}")

# Find accounts with balance > 50000
print("\nHigh Balance Accounts (> ₹50,000):")
cursor.execute(
    "SELECT * FROM accounts WHERE balance > ?",
    (50000,)
)
high_balance = cursor.fetchall()

for account in high_balance:
    print(f"  {account[0]}: {account[1]} - ₹{account[2]:,.2f}")

conn.close()

# Output:
# Account Found:
#   Number: ACC001
#   Holder: Rajesh Kumar
#   Balance: ₹50,000.00
#   Type: Savings
#
# Savings Accounts:
#   ACC001: Rajesh Kumar - ₹50,000.00
#   ACC003: Amit Patel - ₹30,000.00
#
# High Balance Accounts (> ₹50,000):
#   ACC002: Priya Sharma - ₹75,000.00
#   ACC004: Sneha Gupta - ₹100,000.00