from pydantic import BaseModel

class CardInfo(BaseModel):
    card_number: int
    cardholder_name: str
    expiration_date: str
    cvv: int

class twostepVerificationRequest(BaseModel):
    card_number: int
    cardholder_name: str
    expiration_date: str
    cvv: int

class twostepVerificationResponse(BaseModel):
    verification_code: int

class PaymentRequest(BaseModel):
    card_number: int
    cardholder_name: str
    expiration_date: str
    cvv: int
    verification_code: int
    amount: int

class PaymentResponse(BaseModel):
    status: str
    message: str
