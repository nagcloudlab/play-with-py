"""
Main application using the NPCI package
"""

# Import from our package
from npci.accounts import SavingsAccount, CurrentAccount
from npci.payments import get_gateway
from npci.transactions import Transaction, TransactionHistory
from npci.utils import *



def main():
    print("\n" + "="*70)
    print("NPCI PAYMENT SYSTEM - PACKAGE VERSION")
    print("="*70 + "\n")
    
    # Create accounts
    print("Creating accounts...")
    acc1 = SavingsAccount("SAV001234567", "Rajesh Kumar", 75000)
    acc2 = CurrentAccount("CUR009876543", "Priya Enterprises", 150000, 100000)
    
    print(f"✓ {acc1}")
    print(f"✓ {acc2}")
    
    # Initialize transaction history
    history = TransactionHistory()
    
    # UPI Transfer
    print("\n" + "-"*70)
    print("TEST 1: UPI Transfer")
    print("-"*70)
    
    upi = get_gateway('UPI')
    amount = 25000
    
    print(f"Transfer ₹{amount:,} from {acc1.holder_name} to {acc2.holder_name}")
    success, msg = upi.process(amount, acc1, acc2)
    
    if success:
        print(f"✓ {msg}")
        txn = Transaction(amount, acc1.account_number, acc2.account_number, "UPI")
        txn.mark_success()
        history.add(txn)
    else:
        print(f"✗ {msg}")
    
    # IMPS Transfer
    print("\n" + "-"*70)
    print("TEST 2: IMPS Transfer")
    print("-"*70)
    
    imps = get_gateway('IMPS')
    amount = 50000
    
    print(f"Transfer ₹{amount:,} from {acc2.holder_name} to {acc1.holder_name}")
    success, msg = imps.process(amount, acc2, acc1)
    
    if success:
        print(f"✓ {msg}")
        txn = Transaction(amount, acc2.account_number, acc1.account_number, "IMPS")
        txn.mark_success()
        history.add(txn)
    else:
        print(f"✗ {msg}")
    
    # NEFT Transfer
    print("\n" + "-"*70)
    print("TEST 3: NEFT Transfer")
    print("-"*70)
    
    neft = get_gateway('NEFT')
    amount = 100000
    
    print(f"Transfer ₹{amount:,} from {acc2.holder_name} to {acc1.holder_name}")
    success, msg = neft.process(amount, acc2, acc1)
    
    if success:
        print(f"✓ {msg}")
        txn = Transaction(amount, acc2.account_number, acc1.account_number, "NEFT")
        txn.mark_success()
        history.add(txn)
    else:
        print(f"✗ {msg}")
    
    # Show final balances
    print("\n" + "="*70)
    print("FINAL BALANCES")
    print("="*70)
    print(f"{acc1}")
    print(f"{acc2}")
    
    # Transaction summary
    print("\n" + "="*70)
    print("TRANSACTION SUMMARY")
    print("="*70)
    print(f"Total transactions: {len(history.transactions)}")
    print(f"Successful: {len(history.get_successful())}")
    print(f"Failed: {len(history.get_failed())}")
    print(f"Total volume: {utils.format_currency(history.get_total_volume())}")
    
    print("\nRecent transactions:")
    for txn in history.get_recent(5):
        print(f"  {txn}")
    
    # Show transactions by type
    print("\nTransactions by type:")
    for trans_type in ['UPI', 'IMPS', 'NEFT']:
        txns = history.get_by_type(trans_type)
        if txns:
            total = sum(t.amount for t in txns)
            print(f"  {trans_type}: {len(txns)} transactions, {utils.format_currency(total)}")
    
    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    main()