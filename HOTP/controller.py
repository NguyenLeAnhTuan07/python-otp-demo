from hotp_generator import generate_otp
from hotp_verifier import verify_otp
import time

def main():
    secret = b"12345678901234567890"

    # Đọc counter đúng kiểu
    with open("counter.txt", "r", encoding="utf-8") as f:
        counter = int(f.read().strip())

    shared_data = {}

    generate_otp(secret, counter, shared_data)

    time.sleep(1)

    while True:
        user_otp = input("Enter OTP: ")
        valid, counter = verify_otp(user_otp, secret, counter)

        if valid:
            print("✅ OTP hợp lệ")
            with open("counter.txt", "w", encoding="utf-8") as f:
                f.write(str(counter))
            break
        else:
            print("❌ OTP không hợp lệ")

if __name__ == "__main__":
    main()
