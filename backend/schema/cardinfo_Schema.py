from pydantic import BaseModel

class twostepVerificationRequest(BaseModel):
    account_number: str
    cardholder_name: str
    expiration_date: str
    cvv: int
class twostepVerificationResponse(BaseModel):
    verification_code: int


class PaymentRequest(BaseModel):
    account_number: str
    cardholder_name: str
    expiration_date: str
    cvv: int
    verification_code: int
    amount: int

class PaymentResponse(BaseModel):
    status: str
    message: str


class BalanceRequest(BaseModel):
    account_number: str
    verification_code: int
class BalanceResponse(BaseModel):
    account_number: str
    balance: int

class WithdrawRequest(BaseModel):
    account_number: str
    verification_code: int
    amount: int
class WithdrawResponse(BaseModel):
    message: str
    new_balance: int

class DepositRequest(BaseModel):
    account_number: str
    verification_code: int
    amount: int
class DepositResponse(BaseModel):
    message: str
    new_balance: int

class transferRequest(BaseModel):
    from_account_number: str
    to_account_number: str
    verification_code: int
    amount: int
class transferResponse(BaseModel):
    message: str
    new_balance: int