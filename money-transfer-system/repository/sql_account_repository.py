
import psycopg2

class SQLAccountRepository:
    def __init__(self, db_config):
        self.connection = psycopg2.connect(**db_config)

    def get_account(self, acc_number):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT acc_number, balance FROM ACCOUNTS WHERE acc_number = %s", (acc_number,))
            result = cursor.fetchone()
            if result:
                return {'acc_number': result[0], 'balance': result[1]}
            return None

    def update_account_balance(self, acc_number, new_balance):
        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE ACCOUNTS SET balance = %s WHERE acc_number = %s", (new_balance, acc_number))
            self.connection.commit()