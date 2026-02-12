A Python implementation of HOTP (RFC 4226) and TOTP (RFC 6238), designed for educational purposes.
This project simulates a real-world OTP authentication flow using a modular architecture:

- OTP Generator

- OTP Verifier

- Controller (Coordinator)

The system demonstrates how one-time passwords are generated, rotated, and verified securely.

---

## How to Run
Step 1: Run the controller.
python controller.py
Step 2: The program will generate an OTP automatically.
You will see something like:
Enter OTP:
Step 3: Enter the OTP.
You can obtain the OTP from: otp.txt

---

Important Note

This project is built for educational and demonstration purposes only.

The following are intentionally simplified:

- OTP is written in plaintext to otp.txt

- No rate limiting

- No secure storage

- No production-level security hardening

Do NOT use this implementation in a real production environment.

Thank you for checking out this project.  
Have a great day! ☀️

**Author:** Nguyen Le Anh Tuan

