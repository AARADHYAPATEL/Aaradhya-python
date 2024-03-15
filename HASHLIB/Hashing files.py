import hashlib


def calculate_file_hash(file_path, algorithm='sha256'):
    # Choose the hash algorithm
    hash_algorithm = getattr(hashlib, algorithm)()

    # Read the file in binary mode and update the hash object
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_algorithm.update(chunk)

    # Get the hexadecimal representation of the hash value
    hash_value = hash_algorithm.hexdigest()
    return hash_value


# Example usage
file_path = 'key.txt'
file_hash = calculate_file_hash(file_path)
print("SHA-256 Hash of the file:", file_hash)
