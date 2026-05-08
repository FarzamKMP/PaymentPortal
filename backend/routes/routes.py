from fastapi import FastAPI, HTTPException
from services.transaction import BankSystem
from schema.cardinfo_Schema import BalanceResponse, BalanceRequest, twostepVerificationRequest, twostepVerificationResponse, WithdrawRequest, WithdrawResponse, DepositRequest, DepositResponse, transferRequest, transferResponse
from security.twostepauth import create_otp_for_card, verify_otp_for_card

app = FastAPI()

@app.post("/two_factor_authentication/", response_model=twostepVerificationResponse)
def two_factor_authentication(request: twostepVerificationRequest):
    otp = create_otp_for_card(request.account_number)
    return twostepVerificationResponse(verification_code=otp)

@app.post("/get_balance/", response_model=BalanceResponse)
def get_balance(request: BalanceRequest):
    if not verify_otp_for_card(request.account_number, request.verification_code):
        raise HTTPException(status_code=401, detail="Invalid or expired verification code")

    bank_system = BankSystem()
    balance = bank_system.get_account_balance(request.account_number)
    return BalanceResponse(account_number=request.account_number, balance=balance)

@app.post("/withdraw/", response_model=WithdrawResponse)
def withdraw(request: WithdrawRequest):
    if not verify_otp_for_card(request.account_number, request.verification_code):
        raise HTTPException(status_code=401, detail="Invalid or expired verification code")

    bank_system = BankSystem()
    try:
        new_balance = bank_system.withdraw(request.account_number, request.amount)
        return WithdrawResponse(message="Withdrawal successful", new_balance=new_balance)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/deposit/", response_model=DepositResponse)
def deposit(request: DepositRequest):
    if not verify_otp_for_card(request.account_number, request.verification_code):
        raise HTTPException(status_code=401, detail="Invalid or expired verification code")

    bank_system = BankSystem()
    try:
        new_balance = bank_system.deposit(request.account_number, request.amount)
        return DepositResponse(message="Deposit successful", new_balance=new_balance)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/transfer/", response_model=transferResponse)
def transfer(request: transferRequest):
    if not verify_otp_for_card(request.from_account_number, request.verification_code):
        raise HTTPException(status_code=401, detail="Invalid or expired verification code")

    bank_system = BankSystem()
    try:
        new_balance = bank_system.transfer(request.from_account_number, request.to_account_number, request.amount)
        return transferResponse(message="Transfer successful", new_balance=new_balance)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))