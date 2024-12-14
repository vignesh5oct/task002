import pyotp
from datetime import datetime, timedelta


secret = pyotp.random_base32()

def generate_otp():
    totp = pyotp.TOTP(secret,interval=30) 
    return totp.now()

def verify_otp(user_otp):
    totp = pyotp.TOTP(secret) 
    is_valid_otp =totp.verify(user_otp)
    return is_valid_otp
