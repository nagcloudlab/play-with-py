# Reading account data
# ====================

def read_account():
    """Read account from file"""
    
    with open("account_data.txt", "r") as file:
        content = file.read()  # Read entire file
        print("File contents:")
        print(content)


read_account()

# Output:
# File contents:
# Account Number: ACC001
# Holder Name: Rajesh Kumar
# Balance: ₹50,000.00