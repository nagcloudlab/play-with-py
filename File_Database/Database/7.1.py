import sqlite3

# Connect to database (creates file if doesn't exist)
conn = sqlite3.connect('npci_bank.db')

# Create cursor (executes SQL commands)
cursor = conn.cursor()

print("✓ Database created: npci_bank.db")
print("✓ Connected to database")

# Close connection
conn.close()
print("✓ Connection closed")

# Output:
# ✓ Database created: npci_bank.db
# ✓ Connected to database
# ✓ Connection closed

# Now you have a file: npci_bank.db on disk