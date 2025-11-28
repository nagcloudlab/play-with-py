import sqlite3

conn = sqlite3.connect('npci_bank.db')
cursor = conn.cursor()

# Delete specific account
cursor.execute("""
    DELETE FROM accounts 
    WHERE account_number = ?
""", ("ACC999",))

conn.commit()
print(f"✓ Deleted {cursor.rowcount} account(s)")

# Delete accounts with zero balance
cursor.execute("""
    DELETE FROM accounts 
    WHERE balance = 0
""")

conn.commit()
print(f"✓ Deleted {cursor.rowcount} zero-balance account(s)")

# ⚠️ DANGEROUS: Delete ALL accounts (use with caution!)
# cursor.execute("DELETE FROM accounts")  # No WHERE clause = deletes everything!

conn.close()

# Output:
# ✓ Deleted 0 account(s)
# ✓ Deleted 0 zero-balance account(s)