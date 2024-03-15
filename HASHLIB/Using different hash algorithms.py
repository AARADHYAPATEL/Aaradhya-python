import hashlib

# Hash a string using different algorithms
string_to_hash = "Hello, World!"

# MD5
md5_hash = hashlib.md5(string_to_hash.encode()).hexdigest()

# SHA1
sha1_hash = hashlib.sha1(string_to_hash.encode()).hexdigest()

# SHA512
sha512_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()

# SHA224
sha224_hash = hashlib.sha224(string_to_hash.encode()).hexdigest()

# SHA384
sha384_hash = hashlib.sha384(string_to_hash.encode()).hexdigest()

print("The string we are hashing:", string_to_hash)
print("MD5 Hash:", md5_hash)
print("SHA1 Hash:", sha1_hash)
print("SHA512 Hash:", sha512_hash)
print("SHA224 Hash:", sha224_hash)
print("SHA384 Hash:", sha384_hash)