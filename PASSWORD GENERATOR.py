import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    try:
        length = int(input("Enter the desired length of the password"))
        if length <= 15:
            print("Length must be positive integer and must be greater than 15")
            return
        password = generate_password(length)
        print("Generated password: ", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length ")


if __name__ == "__main__":
    main()
