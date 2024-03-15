import hashlib

# Hash a password securely using salt
password = "my_password"
salt = "random_salt"

hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
hashed_password_hex = hashed_password.hex()

print("Salted and Hashed Password:", hashed_password_hex)
