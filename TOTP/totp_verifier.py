from totp_generator import totp
import time

def verify_totp(user_otp: str, secret: bytes, window: int = 1):
    now = int(time.time())

    for i in range(-window, window + 1):
        expected = totp(secret, t=now + i * 30)
        if expected == user_otp:
            return True
    return False
