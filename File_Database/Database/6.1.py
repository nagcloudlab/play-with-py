# Problem 1: Finding specific account in large file
# ==================================================

# With 1 million accounts in JSON file:
# - Must load entire file into memory (slow!)
# - Must search through all accounts (slow!)
# - File locks prevent multiple users

import json
import time

def find_account_in_file(account_number):
    """Search in JSON file - SLOW for large data"""
    
    start = time.time()
    
    with open("all_accounts.json", "r") as file:
        accounts = json.load(file)  # Load ALL accounts into memory!
    
    for account in accounts:  # Search through ALL accounts
        if account['account_number'] == account_number:
            elapsed = time.time() - start
            print(f"Found in {elapsed:.4f} seconds")
            return account
    
    elapsed = time.time() - start
    print(f"Not found (searched {len(accounts)} accounts in {elapsed:.4f} seconds)")
    return None


# Problem 2: Complex queries are difficult
# =========================================

# "Find all Savings accounts with balance > 50000 in Mumbai"
# - Need to load all data
# - Write complex Python loops and filters
# - Very inefficient!


# Problem 3: Data integrity issues
# =================================

# Two programs try to update same account simultaneously:
# Program A reads balance: 50000
# Program B reads balance: 50000
# Program A adds 10000, writes: 60000
# Program B adds 5000, writes: 55000
# Expected: 65000, Actual: 55000 ❌