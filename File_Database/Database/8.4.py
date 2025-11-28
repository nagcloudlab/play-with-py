import sqlite3

conn = sqlite3.connect('npci_bank.db')
cursor = conn.cursor()

# Count total accounts
cursor.execute("SELECT COUNT(*) FROM accounts")
total_accounts = cursor.fetchone()[0]
print(f"Total Accounts: {total_accounts}")

# Sum of all balances
cursor.execute("SELECT SUM(balance) FROM accounts")
total_balance = cursor.fetchone()[0]
print(f"Total Balance: ₹{total_balance:,.2f}")

# Average balance
cursor.execute("SELECT AVG(balance) FROM accounts")
avg_balance = cursor.fetchone()[0]
print(f"Average Balance: ₹{avg_balance:,.2f}")

# Min and Max balance
cursor.execute("SELECT MIN(balance), MAX(balance) FROM accounts")
min_bal, max_bal = cursor.fetchone()
print(f"Min Balance: ₹{min_bal:,.2f}")
print(f"Max Balance: ₹{max_bal:,.2f}")

# Count by account type
print("\nAccounts by Type:")
cursor.execute("""
    SELECT account_type, COUNT(*), SUM(balance) 
    FROM accounts 
    GROUP BY account_type
""")

for acc_type, count, total in cursor.fetchall():
    print(f"  {acc_type}: {count} accounts, Total: ₹{total:,.2f}")

conn.close()

# Output:
# Total Accounts: 4
# Total Balance: ₹255,000.00
# Average Balance: ₹63,750.00
# Min Balance: ₹30,000.00
# Max Balance: ₹100,000.00
#
# Accounts by Type:
#   Current: 2 accounts, Total: ₹175,000.00
#   Savings: 2 accounts, Total: ₹80,000.00