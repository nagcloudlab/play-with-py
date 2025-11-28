class DatabaseConnection:
    """Simulated database connection"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
    
    def connect(self):
        print(f"  → Connecting to {self.db_name}...")
        self.connected = True
        print(f"  ✓ Connected")
    
    def disconnect(self):
        if self.connected:
            print(f"  → Disconnecting from {self.db_name}...")
            self.connected = False
            print(f"  ✓ Disconnected")
    
    def execute(self, query):
        if not self.connected:
            raise Exception("Not connected to database")
        print(f"  → Executing: {query}")
        # Simulate query execution
        if "ERROR" in query:
            raise Exception("Query execution failed")
        print(f"  ✓ Query executed")


def update_account_balance(account_number, new_balance):
    """Update account balance with proper connection handling"""
    
    print(f"\n{'='*60}")
    print(f"Updating account {account_number} balance to ₹{new_balance:,.2f}")
    print(f"{'='*60}")
    
    db = DatabaseConnection("npci_accounts.db")
    
    try:
        # Connect to database
        db.connect()
        
        # Execute update query
        query = f"UPDATE accounts SET balance = {new_balance} WHERE account_number = '{account_number}'"
        db.execute(query)
        
        print(f"\n✓ Account balance updated successfully")
        return True
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False
        
    finally:
        # ALWAYS disconnect, even if error occurred
        print(f"\nCleanup:")
        db.disconnect()


# Testing
# =======

# Test 1: Successful update
update_account_balance("ACC001", 50000)
# Output:
# ============================================================
# Updating account ACC001 balance to ₹50,000.00
# ============================================================
#   → Connecting to npci_accounts.db...
#   ✓ Connected
#   → Executing: UPDATE accounts SET balance = 50000 WHERE account_number = 'ACC001'
#   ✓ Query executed
# 
# ✓ Account balance updated successfully
# 
# Cleanup:
#   → Disconnecting from npci_accounts.db...
#   ✓ Disconnected

# Test 2: Query fails, but connection still closes
update_account_balance("ERROR_ACC", 25000)
# Output:
# ============================================================
# Updating account ERROR_ACC balance to ₹25,000.00
# ============================================================
#   → Connecting to npci_accounts.db...
#   ✓ Connected
#   → Executing: UPDATE accounts SET balance = 25000 WHERE account_number = 'ERROR_ACC'
# 
# ✗ Error: Query execution failed
# 
# Cleanup:
#   → Disconnecting from npci_accounts.db...
#   ✓ Disconnected  ← Still disconnected even with error!