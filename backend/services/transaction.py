from query.queries import get_balance, update_balance, withdraw, deposit

class BankSystem:
    def __init__(self):
        pass

    def get_account_balance(self, account_number):
        return get_balance(account_number)

    def _update_account_balance(self, account_id, new_balance):
        update_balance(account_id, new_balance)

    def withdraw(self, account_id, amount):
        if amount <= 0:
            return "Amount must be positive"
        return withdraw(account_id, amount)

    def deposit(self, account_id, amount):
        if amount <= 0:
            return "Amount must be positive"
        return deposit(account_id, amount)