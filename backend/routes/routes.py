from fastapi import FastAPI
from services.transaction import BankSystem
from schema.cardinfo_Schema import BalanceResponse

app = FastAPI()

@app.post("/get_balance/", response_model=BalanceResponse)
def get_balance(account_id: int):
    bank_system = BankSystem()
    balance = bank_system.get_balance(account_id)
    return BalanceResponse(account_id=account_id, balance=balance)