# Reading line by line
# ====================

def read_account_lines():
    """Read account line by line"""
    
    with open("account_data.txt", "r") as file:
        for line_num, line in enumerate(file, 1):
            print(f"Line {line_num}: {line.strip()}")


read_account_lines()

# Output:
# Line 1: Account Number: ACC001
# Line 2: Holder Name: Rajesh Kumar
# Line 3: Balance: ₹50,000.00