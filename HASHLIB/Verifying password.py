import hashlib

# Verify a password against a stored hash
stored_hash = "stored_hashed_password"


def verify_password(password, stored_hash):
    input_hash = hashlib.sha256(password.encode()).hexdigest()
    if input_hash == stored_hash:
        return True
    else:
        return False


password_to_verify = "password_to_verify"
if verify_password(password_to_verify, stored_hash):
    print("Password is correct!")
else:
    print("Password is incorrect.")
