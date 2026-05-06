import random

def generate_otp(length=5):
    """Generates a random OTP of specified length."""
    otp = ''.join(random.choices('0123456789', k=length))
    print (f"Generated OTP: {otp}")  # For debugging purposes, remove in production
    return otp

generate_otp()