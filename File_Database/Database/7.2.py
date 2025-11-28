import sqlite3

conn = sqlite3.connect('npci_bank.db')
cursor = conn.cursor()

# Create accounts table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        account_number TEXT PRIMARY KEY,
        holder_name TEXT NOT NULL,
        balance REAL NOT NULL,
        account_type TEXT NOT NULL,
        created_date TEXT
    )
''')

print("✓ Table 'accounts' created")

# Save changes
conn.commit()

# Close connection
conn.close()

# Output:
# ✓ Table 'accounts' created