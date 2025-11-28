import sqlite3
from datetime import datetime
from contextlib import contextmanager

class BankDatabase:
    """Complete banking system with database"""
    
    def __init__(self, db_name='npci_bank.db'):
        self.db_name = db_name
        self.initialize_database()
    
    @contextmanager
    def get_connection(self):
        """Context manager for database connections"""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row  # Access columns by name
        try:
            yield conn
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
    
    def initialize_database(self):
        """Create tables if they don't exist"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Accounts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS accounts (
                    account_number TEXT PRIMARY KEY,
                    holder_name TEXT NOT NULL,
                    email TEXT,
                    phone TEXT,
                    balance REAL NOT NULL DEFAULT 0,
                    account_type TEXT NOT NULL,
                    status TEXT DEFAULT 'ACTIVE',
                    created_date TEXT NOT NULL
                )
            ''')
            
            # Transactions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    sender_account TEXT NOT NULL,
                    receiver_account TEXT NOT NULL,
                    amount REAL NOT NULL,
                    transaction_type TEXT NOT NULL,
                    status TEXT NOT NULL,
                    description TEXT,
                    FOREIGN KEY (sender_account) REFERENCES accounts(account_number),
                    FOREIGN KEY (receiver_account) REFERENCES accounts(account_number)
                )
            ''')
            
            # Create indexes for faster queries
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_transactions_sender 
                ON transactions(sender_account)
            ''')
            
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_transactions_receiver 
                ON transactions(receiver_account)
            ''')
            
            conn.commit()
            print("✓ Database initialized")
    
    def create_account(self, account_number, holder_name, initial_balance, account_type, email=None, phone=None):
        """Create new account"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            try:
                cursor.execute('''
                    INSERT INTO accounts 
                    (account_number, holder_name, email, phone, balance, account_type, created_date)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (account_number, holder_name, email, phone, initial_balance, account_type, datetime.now().isoformat()))
                
                conn.commit()
                print(f"✓ Account created: {account_number} - {holder_name}")
                return True
                
            except sqlite3.IntegrityError:
                print(f"✗ Account {account_number} already exists")
                return False
    
    def get_account(self, account_number):
        """Get account details"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (account_number,))
            return cursor.fetchone()
    
    def transfer(self, sender_acc, receiver_acc, amount, description=""):
        """Transfer money between accounts"""
        
        timestamp = datetime.now().isoformat()
        
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            try:
                # Validate sender
                cursor.execute(
                    "SELECT holder_name, balance, status FROM accounts WHERE account_number = ?",
                    (sender_acc,)
                )
                sender = cursor.fetchone()
                
                if not sender:
                    raise ValueError(f"Sender account {sender_acc} not found")
                
                if sender['status'] != 'ACTIVE':
                    raise ValueError(f"Sender account is {sender['status']}")
                
                if sender['balance'] < amount:
                    raise ValueError(f"Insufficient balance")
                
                # Validate receiver
                cursor.execute(
                    "SELECT holder_name, status FROM accounts WHERE account_number = ?",
                    (receiver_acc,)
                )
                receiver = cursor.fetchone()
                
                if not receiver:
                    raise ValueError(f"Receiver account {receiver_acc} not found")
                
                if receiver['status'] != 'ACTIVE':
                    raise ValueError(f"Receiver account is {receiver['status']}")
                
                # Perform transfer
                cursor.execute(
                    "UPDATE accounts SET balance = balance - ? WHERE account_number = ?",
                    (amount, sender_acc)
                )
                
                cursor.execute(
                    "UPDATE accounts SET balance = balance + ? WHERE account_number = ?",
                    (amount, receiver_acc)
                )
                
                # Log transaction
                cursor.execute('''
                    INSERT INTO transactions 
                    (timestamp, sender_account, receiver_account, amount, transaction_type, status, description)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (timestamp, sender_acc, receiver_acc, amount, "TRANSFER", "SUCCESS", description))
                
                txn_id = cursor.lastrowid
                
                conn.commit()
                
                print(f"✓ Transfer successful (TXN-{txn_id})")
                print(f"  ₹{amount:,.2f} from {sender_acc} to {receiver_acc}")
                
                return True, txn_id
                
            except Exception as e:
                # Log failed transaction
                try:
                    cursor.execute('''
                        INSERT INTO transactions 
                        (timestamp, sender_account, receiver_account, amount, transaction_type, status, description)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (timestamp, sender_acc, receiver_acc, amount, "TRANSFER", "FAILED", str(e)))
                    conn.commit()
                except:
                    pass
                
                print(f"✗ Transfer failed: {e}")
                return False, None
    
    def get_balance(self, account_number):
        """Get current balance"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
            result = cursor.fetchone()
            return result['balance'] if result else None
    
    def get_statement(self, account_number, limit=10):
        """Get account statement"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Get account info
            account = self.get_account(account_number)
            if not account:
                print(f"✗ Account {account_number} not found")
                return
            
            print(f"\n{'='*80}")
            print(f"ACCOUNT STATEMENT")
            print(f"{'='*80}")
            print(f"Account Number: {account['account_number']}")
            print(f"Account Holder: {account['holder_name']}")
            print(f"Account Type: {account['account_type']}")
            print(f"Current Balance: ₹{account['balance']:,.2f}")
            print(f"Status: {account['status']}")
            print(f"{'='*80}\n")
            
            # Get recent transactions
            cursor.execute('''
                SELECT * FROM transactions
                WHERE sender_account = ? OR receiver_account = ?
                ORDER BY timestamp DESC
                LIMIT ?
            ''', (account_number, account_number, limit))
            
            transactions = cursor.fetchall()
            
            if transactions:
                print("Recent Transactions:")
                print("-" * 80)
                
                for txn in transactions:
                    dt = datetime.fromisoformat(txn['timestamp'])
                    date_str = dt.strftime("%Y-%m-%d %H:%M:%S")
                    
                    if txn['sender_account'] == account_number:
                        txn_type = "DEBIT"
                        other = txn['receiver_account']
                        sign = "-"
                    else:
                        txn_type = "CREDIT"
                        other = txn['sender_account']
                        sign = "+"
                    
                    print(f"[{date_str}] TXN-{txn['transaction_id']} [{txn['status']}]")
                    print(f"  {txn_type}: {sign}₹{txn['amount']:,.2f} ({other})")
                    if txn['description']:
                        print(f"  Description: {txn['description']}")
                    print()
            else:
                print("No transactions found")
            
            print(f"{'='*80}\n")
    
    def list_all_accounts(self):
        """List all accounts"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM accounts ORDER BY holder_name")
            accounts = cursor.fetchall()
            
            print(f"\n{'='*80}")
            print(f"ALL ACCOUNTS")
            print(f"{'='*80}")
            
            for acc in accounts:
                print(f"{acc['account_number']}: {acc['holder_name']}")
                print(f"  Balance: ₹{acc['balance']:,.2f} | Type: {acc['account_type']} | Status: {acc['status']}")
            
            print(f"{'='*80}")
            print(f"Total: {len(accounts)} accounts")
            print(f"{'='*80}\n")


# ============================================================================
# COMPLETE DEMO
# ============================================================================

print("NPCI BANKING SYSTEM WITH DATABASE")
print("="*80)

# Initialize database
bank = BankDatabase()

# Create accounts
bank.create_account("ACC001", "Rajesh Kumar", 100000, "Savings", "rajesh@example.com", "+91-9876543210")
bank.create_account("ACC002", "Priya Sharma", 150000, "Current", "priya@example.com", "+91-9876543211")
bank.create_account("ACC003", "Amit Patel", 75000, "Savings", "amit@example.com", "+91-9876543212")
bank.create_account("ACC004", "Sneha Gupta", 200000, "Current", "sneha@example.com", "+91-9876543213")

# List all accounts
bank.list_all_accounts()

# Perform transfers
print("\nProcessing Transfers:")
print("-"*80)
bank.transfer("ACC001", "ACC002", 25000, "Payment for services")
bank.transfer("ACC002", "ACC003", 40000, "Loan repayment")
bank.transfer("ACC003", "ACC004", 15000, "Investment")
bank.transfer("ACC004", "ACC001", 50000, "Refund")

# Try failed transfer
bank.transfer("ACC001", "ACC999", 5000, "Invalid transfer")

# Check balances
print("\nCurrent Balances:")
print("-"*80)
for acc_num in ["ACC001", "ACC002", "ACC003", "ACC004"]:
    balance = bank.get_balance(acc_num)
    print(f"{acc_num}: ₹{balance:,.2f}")

# Generate statements
bank.get_statement("ACC001")
bank.get_statement("ACC002")

print("\n✓ Complete banking system with database operational!")
print("  All data persisted to: npci_bank.db")
# ```

# ---

## **Summary: File Handling & Databases**

### Key Takeaways:

# **File Handling:**
# 1. ✓ Use `with` statement for automatic closing
# 2. ✓ CSV for tabular data (accounts, reports)
# 3. ✓ JSON for nested/complex data (configurations)
# 4. ✓ Text files for logs and simple data

# **Databases:**
# 1. ✓ SQLite for persistent, queryable data
# 2. ✓ Use transactions for data integrity
# 3. ✓ Always use `?` placeholders (SQL injection prevention)
# 4. ✓ Create indexes for fast queries
# 5. ✓ Log all financial transactions (audit trail)

### When to Use What:
# ```
# Use Files When:
# - Simple data
# - Small datasets (< 1000 records)
# - One-time exports/imports
# - Configuration files
# - Log files

# Use Databases When:
# - Complex queries needed
# - Large datasets (> 1000 records)
# - Multiple concurrent users
# - Data relationships
# - Financial transactions
# - Need ACID guarantees