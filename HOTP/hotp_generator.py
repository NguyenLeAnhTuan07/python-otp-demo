import hmac
import hashlib
import struct
import threading
import time

def hotp(secret: bytes, counter: int, digits: int = 6) -> str:
    counter_bytes = struct.pack(">Q", counter)
    hmac_hash = hmac.new(secret, counter_bytes, hashlib.sha1).digest()

    offset = hmac_hash[-1] & 0x0F
    binary = (
        ((hmac_hash[offset] & 0x7F) << 24) |
        ((hmac_hash[offset + 1] & 0xFF) << 16) |
        ((hmac_hash[offset + 2] & 0xFF) << 8) |
        (hmac_hash[offset + 3] & 0xFF)
    )

    otp = binary % (10 ** digits)
    return f"{otp:06d}"


def write_to_file(otp: str):
    with open("otp.txt", "w") as f:
        f.write(otp)


def generate_otp(secret, counter, shared_data):
    otp = hotp(secret, counter)
    print(f"[GENERATOR] OTP generated")

    # Luồng 1: gửi OTP cho controller
    shared_data["otp"] = otp

    # Luồng 2: ghi OTP ra file
    t = threading.Thread(target=write_to_file, args=(otp,))
    t.start()
    t.join()
