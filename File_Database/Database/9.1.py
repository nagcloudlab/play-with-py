import sqlite3

conn = sqlite3.connect('npci_bank.db')
cursor = conn.cursor()

# Get current balance
cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", ("ACC001",))
old_balance = cursor.fetchone()[0]
print(f"Old Balance: ₹{old_balance:,.2f}")

# Update balance
new_balance = old_balance + 10000
cursor.execute("""
    UPDATE accounts 
    SET balance = ? 
    WHERE account_number = ?
""", (new_balance, "ACC001"))

conn.commit()

# Verify update
cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", ("ACC001",))
updated_balance = cursor.fetchone()[0]
print(f"New Balance: ₹{updated_balance:,.2f}")
print(f"✓ Updated {cursor.rowcount} row(s)")

conn.close()

# Output:
# Old Balance: ₹50,000.00
# New Balance: ₹60,000.00
# ✓ Updated 1 row(s)