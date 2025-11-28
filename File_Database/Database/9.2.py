import sqlite3

def transfer_money(sender_acc, receiver_acc, amount):
    """Transfer money between accounts using database"""
    
    conn = sqlite3.connect('npci_bank.db')
    cursor = conn.cursor()
    
    try:
        # Start transaction
        
        # Check sender balance
        cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?",
            (sender_acc,)
        )
        result = cursor.fetchone()
        if not result:
            print(f"✗ Sender account {sender_acc} not found")
            return False
        
        sender_balance = result[0]
        
        if sender_balance < amount:
            print(f"✗ Insufficient balance. Available: ₹{sender_balance:,.2f}")
            return False
        
        # Check receiver exists
        cursor.execute(
            "SELECT account_number FROM accounts WHERE account_number = ?",
            (receiver_acc,)
        )
        if not cursor.fetchone():
            print(f"✗ Receiver account {receiver_acc} not found")
            return False
        
        # Deduct from sender
        cursor.execute("""
            UPDATE accounts 
            SET balance = balance - ? 
            WHERE account_number = ?
        """, (amount, sender_acc))
        
        # Add to receiver
        cursor.execute("""
            UPDATE accounts 
            SET balance = balance + ? 
            WHERE account_number = ?
        """, (amount, receiver_acc))
        
        # Commit transaction
        conn.commit()
        
        print(f"✓ Transferred ₹{amount:,.2f} from {sender_acc} to {receiver_acc}")
        
        # Show new balances
        cursor.execute(
            "SELECT balance FROM accounts WHERE account_number IN (?, ?)",
            (sender_acc, receiver_acc)
        )
        balances = cursor.fetchall()
        print(f"  {sender_acc} new balance: ₹{balances[0][0]:,.2f}")
        print(f"  {receiver_acc} new balance: ₹{balances[1][0]:,.2f}")
        
        return True
        
    except Exception as e:
        # Rollback on error
        conn.rollback()
        print(f"✗ Transfer failed: {e}")
        return False
        
    finally:
        conn.close()


# Test transfers
transfer_money("ACC001", "ACC002", 5000)
transfer_money("ACC003", "ACC004", 10000)
transfer_money("ACC001", "ACC999", 1000)  # Non-existent account

# Output:
# ✓ Transferred ₹5,000.00 from ACC001 to ACC002
#   ACC001 new balance: ₹55,000.00
#   ACC002 new balance: ₹80,000.00
# ✓ Transferred ₹10,000.00 from ACC003 to ACC004
#   ACC003 new balance: ₹20,000.00
#   ACC004 new balance: ₹110,000.00
# ✗ Receiver account ACC999 not found