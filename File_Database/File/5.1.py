import json
import csv
from datetime import datetime

class Account:
    """Account with file persistence"""
    
    def __init__(self, account_number, holder_name, balance, account_type):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.account_type = account_type
    
    def to_dict(self):
        """Convert to dictionary for JSON"""
        return {
            'account_number': self.account_number,
            'holder_name': self.holder_name,
            'balance': self.balance,
            'account_type': self.account_type
        }
    
    @staticmethod
    def from_dict(data):
        """Create Account from dictionary"""
        return Account(
            data['account_number'],
            data['holder_name'],
            data['balance'],
            data['account_type']
        )
    
    def __str__(self):
        return f"{self.holder_name} ({self.account_number}): ₹{self.balance:,.2f} [{self.account_type}]"


class AccountManager:
    """Manages accounts with file persistence"""
    
    def __init__(self, accounts_file="accounts.json", transactions_file="transactions.csv"):
        self.accounts_file = accounts_file
        self.transactions_file = transactions_file
        self.accounts = {}
        self.load_accounts()
    
    def load_accounts(self):
        """Load accounts from JSON file"""
        try:
            with open(self.accounts_file, "r") as file:
                data = json.load(file)
                for acc_data in data:
                    acc = Account.from_dict(acc_data)
                    self.accounts[acc.account_number] = acc
            print(f"✓ Loaded {len(self.accounts)} accounts")
        except FileNotFoundError:
            print("ℹ No existing accounts file, starting fresh")
            self.accounts = {}
    
    def save_accounts(self):
        """Save all accounts to JSON file"""
        data = [acc.to_dict() for acc in self.accounts.values()]
        with open(self.accounts_file, "w") as file:
            json.dump(data, file, indent=4)
        print(f"✓ Saved {len(self.accounts)} accounts")
    
    def create_account(self, account_number, holder_name, initial_balance, account_type):
        """Create new account"""
        if account_number in self.accounts:
            print(f"✗ Account {account_number} already exists")
            return None
        
        account = Account(account_number, holder_name, initial_balance, account_type)
        self.accounts[account_number] = account
        self.save_accounts()
        
        print(f"✓ Created account: {account}")
        return account
    
    def get_account(self, account_number):
        """Get account by number"""
        return self.accounts.get(account_number)
    
    def transfer(self, sender_num, receiver_num, amount):
        """Transfer money between accounts"""
        
        # Get accounts
        sender = self.get_account(sender_num)
        receiver = self.get_account(receiver_num)
        
        if not sender:
            print(f"✗ Sender account {sender_num} not found")
            return False
        
        if not receiver:
            print(f"✗ Receiver account {receiver_num} not found")
            return False
        
        # Validate
        if amount <= 0:
            print("✗ Invalid amount")
            return False
        
        if sender.balance < amount:
            print(f"✗ Insufficient balance in {sender_num}")
            return False
        
        # Perform transfer
        sender.balance -= amount
        receiver.balance += amount
        
        # Save accounts
        self.save_accounts()
        
        # Log transaction
        self.log_transaction(sender_num, receiver_num, amount, "SUCCESS")
        
        print(f"✓ Transferred ₹{amount:,.2f} from {sender_num} to {receiver_num}")
        return True
    
    def log_transaction(self, sender, receiver, amount, status):
        """Log transaction to CSV file"""
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txn_id = f"TXN{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Append to CSV
        with open(self.transactions_file, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([txn_id, timestamp, sender, receiver, amount, status])
    
    def generate_statement(self, account_number):
        """Generate account statement from transaction log"""
        
        account = self.get_account(account_number)
        if not account:
            print(f"✗ Account {account_number} not found")
            return
        
        print(f"\n{'='*70}")
        print(f"ACCOUNT STATEMENT: {account_number}")
        print(f"{'='*70}")
        print(f"Holder: {account.holder_name}")
        print(f"Type: {account.account_type}")
        print(f"Current Balance: ₹{account.balance:,.2f}")
        print(f"{'='*70}")
        print(f"Recent Transactions:")
        print(f"{'-'*70}")
        
        try:
            with open(self.transactions_file, "r") as file:
                reader = csv.reader(file)
                transactions = []
                
                for row in reader:
                    txn_id, timestamp, sender, receiver, amount, status = row
                    
                    if sender == account_number or receiver == account_number:
                        txn_type = "DEBIT" if sender == account_number else "CREDIT"
                        other_acc = receiver if sender == account_number else sender
                        transactions.append({
                            'id': txn_id,
                            'timestamp': timestamp,
                            'type': txn_type,
                            'amount': float(amount),
                            'other': other_acc,
                            'status': status
                        })
                
                if not transactions:
                    print("  No transactions found")
                else:
                    for txn in transactions[-10:]:  # Last 10 transactions
                        sign = "-" if txn['type'] == "DEBIT" else "+"
                        print(f"  [{txn['timestamp']}] {txn['id']}")
                        print(f"    {txn['type']}: {sign}₹{txn['amount']:,.2f} ({txn['other']}) [{txn['status']}]")
        
        except FileNotFoundError:
            print("  No transactions found")
        
        print(f"{'='*70}\n")
    
    def list_all_accounts(self):
        """List all accounts"""
        print(f"\n{'='*70}")
        print(f"ALL ACCOUNTS")
        print(f"{'='*70}")
        
        for acc in self.accounts.values():
            print(f"  {acc}")
        
        print(f"{'='*70}")
        print(f"Total: {len(self.accounts)} accounts")
        print(f"{'='*70}\n")


# ============================================================================
# DEMO: Complete File-Based Banking System
# ============================================================================

print("NPCI File-Based Banking System")
print("="*70)

# Initialize manager
manager = AccountManager()

# Create accounts
manager.create_account("ACC001", "Rajesh Kumar", 100000, "Savings")
manager.create_account("ACC002", "Priya Sharma", 150000, "Current")
manager.create_account("ACC003", "Amit Patel", 75000, "Savings")

# List accounts
manager.list_all_accounts()

# Perform transfers
print("\nProcessing Transfers:")
print("-"*70)
manager.transfer("ACC001", "ACC002", 25000)
manager.transfer("ACC002", "ACC003", 40000)
manager.transfer("ACC003", "ACC001", 15000)

# Generate statements
manager.generate_statement("ACC001")
manager.generate_statement("ACC002")

# List final balances
manager.list_all_accounts()

print("\n✓ All data persisted to files:")
print("  - accounts.json (account data)")
print("  - transactions.csv (transaction log)")
# ```

# **Output:**
# ```
# NPCI File-Based Banking System
# ======================================================================
# ℹ No existing accounts file, starting fresh
# ✓ Created account: Rajesh Kumar (ACC001): ₹100,000.00 [Savings]
# ✓ Saved 1 accounts
# ✓ Created account: Priya Sharma (ACC002): ₹150,000.00 [Current]
# ✓ Saved 2 accounts
# ✓ Created account: Amit Patel (ACC003): ₹75,000.00 [Savings]
# ✓ Saved 3 accounts

# ======================================================================
# ALL ACCOUNTS
# ======================================================================
#   Rajesh Kumar (ACC001): ₹100,000.00 [Savings]
#   Priya Sharma (ACC002): ₹150,000.00 [Current]
#   Amit Patel (ACC003): ₹75,000.00 [Savings]
# ======================================================================
# Total: 3 accounts
# ======================================================================

# Processing Transfers:
# ----------------------------------------------------------------------
# ✓ Saved 3 accounts
# ✓ Transferred ₹25,000.00 from ACC001 to ACC002
# ✓ Saved 3 accounts
# ✓ Transferred ₹40,000.00 from ACC002 to ACC003
# ✓ Saved 3 accounts
# ✓ Transferred ₹15,000.00 from ACC003 to ACC001

# ======================================================================
# ACCOUNT STATEMENT: ACC001
# ======================================================================
# Holder: Rajesh Kumar
# Type: Savings
# Current Balance: ₹90,000.00
# ======================================================================
# Recent Transactions:
# ----------------------------------------------------------------------
#   [2024-01-15 14:30:45] TXN20240115143045
#     DEBIT: -₹25,000.00 (ACC002) [SUCCESS]
#   [2024-01-15 14:30:46] TXN20240115143046
#     CREDIT: +₹15,000.00 (ACC003) [SUCCESS]
# ======================================================================

# ✓ All data persisted to files:
#   - accounts.json (account data)
#   - transactions.csv (transaction log)