import sqlite3

def safe_transfer(sender_acc, receiver_acc, amount):
    """Transfer with automatic rollback on error"""
    
    conn = sqlite3.connect('npci_bank.db')
    cursor = conn.cursor()
    
    try:
        # Begin transaction (implicit)
        print(f"\nProcessing transfer: ₹{amount:,.2f} from {sender_acc} to {receiver_acc}")
        
        # Step 1: Deduct from sender
        print("  → Deducting from sender...")
        cursor.execute("""
            UPDATE accounts 
            SET balance = balance - ? 
            WHERE account_number = ? AND balance >= ?
        """, (amount, sender_acc, amount))
        
        if cursor.rowcount == 0:
            raise ValueError("Insufficient balance or account not found")
        
        # Simulate error (uncomment to test rollback)
        # raise Exception("Simulated network error!")
        
        # Step 2: Add to receiver
        print("  → Adding to receiver...")
        cursor.execute("""
            UPDATE accounts 
            SET balance = balance + ? 
            WHERE account_number = ?
        """, (amount, receiver_acc))
        
        if cursor.rowcount == 0:
            raise ValueError("Receiver account not found")
        
        # Commit transaction
        conn.commit()
        print("  ✓ Transaction committed")
        
        return True
        
    except Exception as e:
        # Rollback on any error
        conn.rollback()
        print(f"  ✗ Transaction rolled back: {e}")
        return False
        
    finally:
        conn.close()


# Test successful transfer
safe_transfer("ACC001", "ACC002", 5000)

# Test failed transfer (insufficient balance)
safe_transfer("ACC003", "ACC004", 50000)

# Verify balances unchanged after failed transfer
conn = sqlite3.connect('npci_bank.db')
cursor = conn.cursor()
cursor.execute("SELECT account_number, balance FROM accounts WHERE account_number = 'ACC003'")
print(f"\nACC003 balance (unchanged): ₹{cursor.fetchone()[1]:,.2f}")
conn.close()

# Output:
# Processing transfer: ₹5,000.00 from ACC001 to ACC002
#   → Deducting from sender...
#   → Adding to receiver...
#   ✓ Transaction committed
#
# Processing transfer: ₹50,000.00 from ACC003 to ACC004
#   → Deducting from sender...
#   ✗ Transaction rolled back: Insufficient balance or account not found
#
# ACC003 balance (unchanged): ₹20,000.00