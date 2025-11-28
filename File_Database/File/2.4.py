# Appending transaction log
# ==========================

def log_transaction(txn_id, sender, receiver, amount, status):
    """Append transaction to log file"""
    
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("transactions.log", "a") as file:  # 'a' for append
        file.write(f"[{timestamp}] {txn_id}: ₹{amount:,.2f} {sender}→{receiver} [{status}]\n")
    
    print(f"✓ Transaction {txn_id} logged")


# Log multiple transactions
log_transaction("TXN001", "ACC001", "ACC002", 5000, "SUCCESS")
log_transaction("TXN002", "ACC003", "ACC004", 3000, "SUCCESS")
log_transaction("TXN003", "ACC005", "ACC006", 7500, "FAILED")

# Output:
# ✓ Transaction TXN001 logged
# ✓ Transaction TXN002 logged
# ✓ Transaction TXN003 logged

# View log file
with open("transactions.log", "r") as file:
    print("\nTransaction Log:")
    print(file.read())

# Output:
# Transaction Log:
# [2024-01-15 14:30:45] TXN001: ₹5,000.00 ACC001→ACC002 [SUCCESS]
# [2024-01-15 14:30:46] TXN002: ₹3,000.00 ACC003→ACC004 [SUCCESS]
# [2024-01-15 14:30:47] TXN003: ₹7,500.00 ACC005→ACC006 [FAILED]