from pydantic import BaseModel

class twostepVerificationRequest(BaseModel):
    account_number: str
    cardholder_name: str
    expiration_date: str
    cvv: int
class twostepVerificationResponse(BaseModel):
    verification_code: int


class FinalVerificationRequest(BaseModel):
    account_number: str
    cardholder_name: str
    expiration_date: str
    cvv: int
    verification_code: int
class FinalVerificationResponse(BaseModel):
    status: bool


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