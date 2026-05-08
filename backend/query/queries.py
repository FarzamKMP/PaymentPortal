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

def safe_withdraw(account_number, amount):
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE accounts SET balance = balance - %s WHERE account_number = %s AND balance >= %s",
        (amount, account_number, amount)
    )
    connection.commit()
    affected = cursor.rowcount
    cursor.close()
    if affected == 0:
        raise ValueError("Insufficient funds or account not found")
    return get_balance(account_number)

def safe_deposit(account_number, amount):
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE accounts SET balance = balance + %s WHERE account_number = %s",
        (amount, account_number)
    )
    connection.commit()
    affected = cursor.rowcount
    cursor.close()
    if affected == 0:
        raise ValueError("Account not found")
    return get_balance(account_number)

def safe_transfer(from_account_number, to_account_number, amount):
    cursor = connection.cursor()
    try:
        cursor.execute(
            "UPDATE accounts SET balance = balance - %s WHERE account_number = %s AND balance >= %s",
            (amount, from_account_number, amount)
        )
        if cursor.rowcount == 0:
            raise ValueError("Insufficient funds or source account not found")

        cursor.execute(
            "UPDATE accounts SET balance = balance + %s WHERE account_number = %s",
            (amount, to_account_number)
        )
        if cursor.rowcount == 0:
            raise ValueError("Destination account not found")

        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
    return get_balance(from_account_number)
    