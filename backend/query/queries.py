from .connection import create_connection


class BankSystem:
    def __init__(self):
        self.connection = create_connection()
        if self.connection is None:
            raise ConnectionError("Failed to connect to the database")

    def get_account_balance(self, account_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else None

    def _update_account_balance(self, account_id, new_balance):
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE accounts SET balance = %s WHERE account_id = %s",
            (new_balance, account_id)
        )
        self.connection.commit()
        cursor.close()

    def withdraw(self, account_id, amount):
        if amount <= 0:
            return "Amount must be positive"
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE accounts SET balance = balance - %s WHERE account_id = %s AND balance >= %s",
            (amount, account_id, amount)
        )
        self.connection.commit()
        affected = cursor.rowcount
        cursor.close()
        if affected == 0:
            return "Account not found or insufficient funds"
        return "Withdrawal successful"

    def deposit(self, account_id, amount):
        if amount <= 0:
            return "Amount must be positive"
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE accounts SET balance = balance + %s WHERE account_id = %s",
            (amount, account_id)
        )
        self.connection.commit()
        affected = cursor.rowcount
        cursor.close()
        if affected == 0:
            return "Account not found"
        return "Deposit successful"

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
