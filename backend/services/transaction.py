from query.queries import get_balance, update_balance, safe_withdraw, safe_deposit, safe_transfer

class BankSystem:
    def __init__(self):
        pass

    def get_account_balance(self, account_number):
        return get_balance(account_number)

    def _update_account_balance(self, account_number, new_balance):
        update_balance(account_number, new_balance)

    def withdraw(self, account_number, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return safe_withdraw(account_number, amount)

    def deposit(self, account_number, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return safe_deposit(account_number, amount)

    def transfer(self, from_account_number, to_account_number, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return safe_transfer(from_account_number, to_account_number, amount)