# With Database:
# ==============

# 1. Fast searches with indexes
# 2. Complex queries with SQL
# 3. Concurrent access with transactions
# 4. Data integrity with constraints
# 5. Relationships between tables

import sqlite3

# Find account - FAST even with millions of records
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM accounts WHERE account_number = ?", ("ACC001",))
account = cursor.fetchone()  # Database finds it instantly using index!

# Complex query - EASY
cursor.execute("""
    SELECT * FROM accounts 
    WHERE account_type = 'Savings' 
      AND balance > 50000 
      AND city = 'Mumbai'
""")