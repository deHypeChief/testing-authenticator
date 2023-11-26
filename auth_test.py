import pyotp
import time

# Replace 'your_secret_key' with the actual secret key obtained during setup
secret_key = 'JBSWY3DPEHPK3PXP'

# Create a TOTP object
totp = pyotp.TOTP(secret_key)

# Generate and print the current TOTP code
current_code = totp.now()
print(f"Current TOTP Code: {current_code}")

# Wait for 30 seconds (or the time step used in your TOTP setup)
time.sleep(30)

# Generate and print the TOTP code after 30 seconds
new_code = totp.now()
print(f"New TOTP Code: {new_code}")