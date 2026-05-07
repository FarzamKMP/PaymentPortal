from fastapi import FastAPI, HTTPException
from services.transaction import BankSystem
from schema.cardinfo_Schema import BalanceResponse, BalanceRequest, twostepVerificationRequest, twostepVerificationResponse
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