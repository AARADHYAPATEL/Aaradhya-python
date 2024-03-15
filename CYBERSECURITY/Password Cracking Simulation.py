import hashlib


def simulate_password_cracking(hashed_password, password_list):
    for password in password_list:
        if hashlib.sha256(password.encode()).hexdigest() == hashed_password:
            return f"Password cracked: {password}"
    return "Password not found"


# Example
hashed_password_to_crack = "b1d7adb4b560f4d0426dc5308c88fd39729a2adf086f6b3fc9104244f71b9c66"
common_passwords = ["password", "mom_dad_uncle", "qwerty", "Kratos_the_spartan"]

result = simulate_password_cracking(hashed_password_to_crack, common_passwords)
print(result)
