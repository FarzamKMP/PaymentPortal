import random
import time

OTP_TTL_SECONDS = 120

# account_number -> (otp, created_at)
_otp_store: dict[int, tuple[int, float]] = {}

def generate_otp(length=5) -> str:
    return ''.join(random.choices('0123456789', k=length))

def create_otp_for_card(account_number: int) -> int:
    otp = int(generate_otp(length=5))
    _otp_store[account_number] = (otp, time.time())
    return otp

def verify_otp_for_card(account_number: int, code: int) -> bool:
    entry = _otp_store.get(account_number)
    if entry is None:
        return False
    otp, created_at = entry
    if time.time() - created_at > OTP_TTL_SECONDS:
        del _otp_store[account_number]
        return False
    if otp == code:
        del _otp_store[account_number]
        return True
    return False