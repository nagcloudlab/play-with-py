

from repository.sql_account_repository import SQLAccountRepository as AccountRepository

class TransferService:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def transfer(self, from_acc_number: str, to_acc_number: str, amount: int) -> bool:
        from_account = self.account_repository.get_account(from_acc_number)
        to_account = self.account_repository.get_account(to_acc_number)

        if not from_account or not to_account:
            return False  # One of the accounts does not exist

        if from_account['balance'] < amount:
            return False  # Insufficient funds

        # Perform the transfer
        new_from_balance = from_account['balance'] - amount
        new_to_balance = to_account['balance'] + amount

        self.account_repository.update_account_balance(from_acc_number, new_from_balance)
        self.account_repository.update_account_balance(to_acc_number, new_to_balance)

        return True