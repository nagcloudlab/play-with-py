

from repository.sql_account_repository import SQLAccountRepository as AccountRepository
from service.transfer_service import TransferService


# create AccountRepository instance with database configuration
db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgrespw',
    'host': 'localhost',
    'port': '55000'
}
account_repository = AccountRepository(db_config)
# create TransferService instance with the repository
transfer_service = TransferService(account_repository)


transfer_service.transfer('ACC456', 'ACC123', 50.0)