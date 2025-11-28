

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

class NoSqlAccountRepository:
    def __init__(self):
        self.accounts = {
            1: Account(1, 1000),
            2: Account(2, 500)
        }  # Simulating a NoSQL database with a dictionary
        print("NoSQL Account Repository Initialized")
    def get_account(self, account_id):
        print(f"Fetching account {account_id} from NoSQL Database")
        return self.accounts.get(account_id)
    def save_account(self, account):
        print(f"Saving account {account.account_id} to NoSQL Database")
        self.accounts[account.account_id] = account

# Factory Class
class AccountRepositoryFactory:
    # Factory Method
    @staticmethod
    def get_account_repository(repo_type):
        if repo_type == "SQL":
            return SqlAccountRepository()
        elif repo_type == "NoSQL":
            return NoSqlAccountRepository()
        else:
            raise ValueError("Unknown repository type")

# -----------------------------------
# Business/Service Layer
# -----------------------------------
# @ team-2

"""

design issues
-------------

    -> dependent & dependency tightly coupled
        => cant't extend with new repository types`
    -> unit-testing is difficult   
        => dev & bug-fixing is difficult

performance issues
------------------

    -> repository creation for every transfer request
        => resource utilization is high
        => response time is high

why these issues?
-------------------

    -> dependent manages the lifecycle of dependency

   Solution:
   ---------
   -> Don't create dependency inside dependent, get from outside(factory) aka Factory Pattern 
    
   issue with factory-only?
   ----------------- ------
   -> on each transfer request, new repository instance is created

    Solution:
    -------------
    -> Don't create & Don't lookup the dependency, 
       inject it from outside 

       a.k.a Dependency Inversion Principle (DIP) / Dependency Injection (DI)

    ------------------------------------
    SOLID Principles of OOP Design
    ------------------------------------

    S -> Single Responsibility Principle (SRP)   
    O -> Open-Closed Principle (OCP)
    L -> Liskov Substitution Principle (LSP)
    I -> Interface Segregation Principle (ISP)
    D -> Dependency Inversion Principle (DIP)

    ------------------------------------

"""

class UPITransferService:
    def __init__(self,account_repositiry):
        self.account_repository = account_repositiry # HAS-A
        print("UPI Transfer Service Initialized")

    def transfer(self, from_account_id, to_account_id, amount):
        print(f"Initiating transfer of {amount} from account {from_account_id} to account {to_account_id}")
        # account_repository = SqlAccountRepository() # create repository instance
        # account_repository = AccountRepositoryFactory.get_account_repository("SQL") # get repository instance from factory
        from_account= self.account_repository.get_account(from_account_id)
        to_account = self.account_repository.get_account(to_account_id)
        if(from_account.balance >= amount):
            from_account.withdraw(amount)
            to_account.deposit(amount)
            self.account_repository.save_account(from_account)
            self.account_repository.save_account(to_account)
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
# create components based configurations 
sql_account_repository = AccountRepositoryFactory.get_account_repository("SQL")
nosql_account_repository = AccountRepositoryFactory.get_account_repository("NoSQL")
transfer_service = UPITransferService(nosql_account_repository) # injecting dependency

print("----------------------------------")
print("Usage of Money Transfer System")
print("----------------------------------")
# perform money transfer
success = transfer_service.transfer(1, 2, 200)
print("Transfer Successful" if success else "Transfer Failed")
print()
success = transfer_service.transfer(2, 1, 800)
print("Transfer Successful" if success else "Transfer Failed")

print("----------------------------------")
print("Destroying Money Transfer System")
print("----------------------------------")
print("End of Day Cleanup Completed")


print("----------------------------------")



class MRFWheel:
    def __init__(self):
        print("MRF Wheel is created")
    def rotate(self):
        print("MRF Wheel is rotating")

class JKWheel:
    def __init__(self):
        print("JK Wheel is created")
    def rotate(self):
        print("JK Wheel is rotating")        

class Car:
    def __init__(self,wheel):
        self.__wheel = wheel
        print("Car is created")

    def set_wheel(self, wheel):
        self.__wheel = wheel
        
    def drive(self):
        self.__wheel.rotate()
        print("Car is moving")


mrf_wheel = MRFWheel()
car = Car(mrf_wheel)
print()
car.drive()
print()
car.drive()

jk_wheel = JKWheel()
car.set_wheel(jk_wheel)
print()
car.drive()
print()
car.drive()
print("----------------------------------")
