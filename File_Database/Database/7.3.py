import sqlite3
from datetime import datetime

conn = sqlite3.connect('npci_bank.db')
cursor = conn.cursor()

# Insert single account
cursor.execute('''
    INSERT INTO accounts (account_number, holder_name, balance, account_type, created_date)
    VALUES (?, ?, ?, ?, ?)
''', ('ACC001', 'Rajesh Kumar', 50000.00, 'Savings', datetime.now().isoformat()))

conn.commit()
print("✓ Account ACC001 inserted")

# Insert multiple accounts
accounts = [
    ('ACC002', 'Priya Sharma', 75000.00, 'Current', datetime.now().isoformat()),
    ('ACC003', 'Amit Patel', 30000.00, 'Savings', datetime.now().isoformat()),
    ('ACC004', 'Sneha Gupta', 100000.00, 'Current', datetime.now().isoformat()),
]

cursor.executemany('''
    INSERT INTO accounts (account_number, holder_name, balance, account_type, created_date)
    VALUES (?, ?, ?, ?, ?)
''', accounts)

conn.commit()
print(f"✓ Inserted {cursor.rowcount} accounts")

conn.close()

# Output:
# ✓ Account ACC001 inserted
# ✓ Inserted 3 accounts