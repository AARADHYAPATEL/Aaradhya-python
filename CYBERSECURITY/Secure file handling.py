import os


def secure_file_detection(file_path):
    with open(file_path, 'w') as file:
        file.write(os.urandom(1024))
        # Overwrite the file with random data
    os.remove(file_path)
    print(f"{file_path} securely deleted")


# Example
file_path_to_delete = "key.txt"
secure_file_detection(file_path_to_delete)