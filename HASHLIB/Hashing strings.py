import hashlib

# Hash a string using SHA256 Algorithm
string_to_hash = "Aaradhya Patel!"
hashed_string = hashlib.sha256(string_to_hash.encode()).hexdigest()

print("Original String:", string_to_hash)
print("Hashed String:", hashed_string)
