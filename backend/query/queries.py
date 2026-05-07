from .connection import create_connection

connection = create_connection()

def get_balance(account_number):
    cursor = connection.cursor()
    cursor.execute("select a.balance from users u join accounts a on u.id = a.user_id where a.account_number = %s;", (account_number,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

def update_balance(account_number, new_balance):
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE accounts SET balance = %s WHERE account_number = %s",
        (new_balance, account_number)
    )
    connection.commit()
    cursor.close()

def withdraw(account_number, amount):
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE accounts SET balance = balance - %s WHERE account_number = %s AND balance >= %s",
        (amount, account_number, amount)
    )
    connection.commit()
    affected = cursor.rowcount
    cursor.close()
    if affected == 0:
        return "Account not found or insufficient funds"
    return "Withdrawal successful"

def deposit(account_number, amount):
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE accounts SET balance = balance + %s WHERE account_number = %s",
        (amount, account_number)
    )
    connection.commit()
    affected = cursor.rowcount
    cursor.close()
    if affected == 0:
        return "Account not found"
    return "Deposit successful"