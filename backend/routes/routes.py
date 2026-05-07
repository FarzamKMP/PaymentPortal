from fastapi import FastAPI
from services.transaction import BankSystem
from schema.cardinfo_Schema import BalanceResponse, BalanceRequest

app = FastAPI()

@app.post("/get_balance/", response_model=BalanceResponse)
def get_balance(request: BalanceRequest):
    bank_system = BankSystem()
    balance = bank_system.get_account_balance(request.account_number)
    return BalanceResponse(account_number=request.account_number, balance=balance)