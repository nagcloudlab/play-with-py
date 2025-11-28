# WITHOUT FILES (Data is lost!)
# =============================

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

# Create accounts
acc1 = Account("ACC001", 50000)
acc2 = Account("ACC002", 30000)

print(f"ACC001 Balance: ₹{acc1.balance:,.2f}")
print(f"ACC002 Balance: ₹{acc2.balance:,.2f}")

# Process transaction
acc1.balance -= 5000
acc2.balance += 5000

print(f"\nAfter transaction:")
print(f"ACC001 Balance: ₹{acc1.balance:,.2f}")
print(f"ACC002 Balance: ₹{acc2.balance:,.2f}")

# Program ends...
# ALL DATA IS LOST! ❌
# Next time program runs, balances are back to original!