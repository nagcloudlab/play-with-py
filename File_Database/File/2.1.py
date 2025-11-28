# Writing account data
# ====================

def save_account(account_number, holder_name, balance):
    """Save single account to file"""
    with open("account_data.txt", "w") as file:
        file.write(f"Account Number: {account_number}\n")
        file.write(f"Holder Name: {holder_name}\n")
        file.write(f"Balance: ₹{balance:,.2f}\n")
    print(f"✓ Account {account_number} saved to file")


# Save account
save_account("ACC001", "Rajesh Kumar", 50000)

# Output:
# ✓ Account ACC001 saved to file

# View the file (on disk):
# Account Number: ACC001
# Holder Name: Rajesh Kumar
# Balance: ₹50,000.00