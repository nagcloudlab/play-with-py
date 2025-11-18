

#----------------------------------
# Money Transfer System
#----------------------------------

#----------------------------------
# Data Model
#----------------------------------

class Account:
    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    

# ----------------------------------
# Data/Repository Layer
# ----------------------------------    
# @ team-1

class SqlAccountRepository:
    def __init__(self):
        self.accounts = {
            1: Account(1, 1000),
            2: Account(2, 500)
        }  # Simulating a database with a dictionary
        print("SQL Account Repository Initialized")
    def get_account(self, account_id):
        print(f"Fetching account {account_id} from SQL Database")
        return self.accounts.get(account_id)
    def save_account(self, account):
        print(f"Saving account {account.account_id} to SQL Database")
        self.accounts[account.account_id] = account

# -----------------------------------
# Business/Service Layer
# -----------------------------------
# @ team-2

class UPITransferService:
    def __init__(self):
        print("UPI Transfer Service Initialized")
    def transfer(self, from_account_id, to_account_id, amount):
        print(f"Initiating transfer of {amount} from account {from_account_id} to account {to_account_id}")
        account_repository = SqlAccountRepository()
        from_account= account_repository.get_account(from_account_id)
        to_account = account_repository.get_account(to_account_id)
        if(from_account.balance >= amount):
            from_account.withdraw(amount)
            to_account.deposit(amount)
            account_repository.save_account(from_account)
            account_repository.save_account(to_account)
            print(f"Transfer of {amount} from account {from_account_id} to account {to_account_id} completed successfully")
            return True
        print(f"Transfer of {amount} from account {from_account_id} to account {to_account_id} failed due to insufficient funds") 
        return False

# -----------------------------------
# Presentation Layer
# -----------------------------------
# @ team-3
print("----------------------------------")
print("initializing Money Transfer System")
print("----------------------------------")
transfer_service = UPITransferService()

print("----------------------------------")
print("Usage of Money Transfer System")
print("----------------------------------")
success = transfer_service.transfer(1, 2, 200)
print("Transfer Successful" if success else "Transfer Failed")
print()
success = transfer_service.transfer(2, 1, 800)
print("Transfer Successful" if success else "Transfer Failed")

print("----------------------------------")
print("Performing End of Day Cleanup")
print("----------------------------------")
print("End of Day Cleanup Completed")

