import hmac
import hashlib
import struct
import time
import threading

TIME_STEP = 30  # giây

def totp(secret: bytes, digits: int = 6, t: int | None = None) -> str:
    if t is None:
        t = int(time.time())

    counter = t // TIME_STEP
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


def generate_totp_loop(secret, shared_data):
    last_counter = None

    while True:
        now = int(time.time())
        counter = now // TIME_STEP

        if counter != last_counter:
            otp = totp(secret, t=now)
            print(f"[GENERATOR] New OTP")
            print("Enter OTP: ")

            shared_data["otp"] = otp

            t = threading.Thread(target=write_to_file, args=(otp,))
            t.start()
            t.join()

            last_counter = counter

        time.sleep(1)
