from hotp_generator import hotp

def verify_otp(user_otp: str, secret: bytes, counter: int, window: int = 5):
    for i in range(window):
        expected = hotp(secret, counter + i)
        if expected == user_otp:
            return True, counter + i + 1
    return False, counter
