from totp_generator import generate_totp_loop
from totp_verifier import verify_totp
import threading

def main():
    secret = b"12345678901234567890"
    shared_data = {}

    # chạy generator ở background
    t = threading.Thread(
        target=generate_totp_loop,
        args=(secret, shared_data),
        daemon=True
    )
    t.start()

    while True:
        user_otp = input()

        if verify_totp(user_otp, secret):
            print("✅ OTP hợp lệ")
            break
        else:
            print("❌ OTP không hợp lệ")

if __name__ == "__main__":
    main()
