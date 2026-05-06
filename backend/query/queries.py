from .connection import create_connection

connection = create_connection()

def get_balance(account_id):
    cursor = connection.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

def update_balance(account_id, new_balance):
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE accounts SET balance = %s WHERE account_id = %s",
        (new_balance, account_id)
    )
    connection.commit()
    cursor.close()

def withdraw(account_id, amount):
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE accounts SET balance = balance - %s WHERE account_id = %s AND balance >= %s",
        (amount, account_id, amount)
    )
    connection.commit()
    affected = cursor.rowcount
    cursor.close()
    if affected == 0:
        return "Account not found or insufficient funds"
    return "Withdrawal successful"

def deposit(account_id, amount):
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE accounts SET balance = balance + %s WHERE account_id = %s",
        (amount, account_id)
    )
    connection.commit()
    affected = cursor.rowcount
    cursor.close()
    if affected == 0:
        return "Account not found"
    return "Deposit successful"