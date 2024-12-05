import json
import os
import bcrypt
import sys
import platform
import openai
from cryptography.fernet import Fernet

# File path for storing user data
USER_DATA_FILE = 'users.json'

# Your OpenAI API key
OPENAI_API_KEY = 'sk-proj-AqtKauW0W4gJandZ36FTT3BlbkFJX7UG3eLloR3tclA3Brkw'


# Function to load the encryption key and users from the JSON file
def load_data():
    if not os.path.exists(USER_DATA_FILE):
        return None, {}

    with open(USER_DATA_FILE, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if 'encryption_key' not in data or 'users' not in data:
        return None, {}

    encryption_key = data['encryption_key'].encode('utf-8')
    users = data['users']
    return encryption_key, users


# Function to save the encryption key and users to the JSON file
def save_data(encryption_key, users):
    data = {
        'encryption_key': encryption_key.decode('utf-8'),
        'users': users
    }
    with open(USER_DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


# Load the encryption key and users
encryption_key, users = load_data()

# Generate a new encryption key if none exists
if encryption_key is None:
    encryption_key = Fernet.generate_key()
    save_data(encryption_key, users)

cipher = Fernet(encryption_key)


# Function to hash a password using bcrypt
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


# Function to check a password against a hashed password
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))


# Function to simulate user registration
def register_user(users):
    print("Register a new user:")
    username = input("Choose a username: ")
    if username in users:
        print("Username already exists. Please try a different one.")
        return users
    while True:
        password = getpass_with_stars("Choose a password: ")
        confirm_password = getpass_with_stars("Confirm password: ")
        if password == confirm_password:
            break
        else:
            print("Passwords do not match. Please try again.")
    hashed_password = hash_password(password).decode('utf-8')
    users[username] = hashed_password
    save_data(encryption_key, users)
    print(f"User {username} registered successfully!")
    return users


# Function to simulate authentication
def authenticate(users):
    print("Login:")
    username = input("Enter username: ")
    password = getpass_with_stars("Enter password: ")
    if username in users and check_password(password, users[username]):
        print("Authentication successful!")
        return True
    else:
        print("Authentication failed. Please try again.")
        return False


# Function to get password input with stars masking
def getpass_with_stars(prompt="Password: "):
    if platform.system() == "Windows":
        import msvcrt
        print(prompt, end='', flush=True)
        password = ""
        while True:
            char = msvcrt.getch()
            if char == b'\r' or char == b'\n':  # Enter key pressed
                print('')
                break
            elif char == b'\x08':  # Backspace pressed
                if len(password) > 0:
                    password = password[:-1]
                    print('\b \b', end='', flush=True)
            else:
                password += char.decode('utf-8')
                print('*', end='', flush=True)
        return password
    else:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            print(prompt, end='', flush=True)
            password = ""
            while True:
                char = sys.stdin.read(1)
                if char == '\r' or char == '\n':  # Enter key pressed
                    print('')
                    break
                elif char == '\x7f':  # Backspace pressed
                    if len(password) > 0:
                        password = password[:-1]
                        print('\b \b', end='', flush=True)
                else:
                    password += char
                    print('*', end='', flush=True)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return password


# Function to handle chatbot interaction using OpenAI API
def chatbot_interaction():
    openai.api_key = OPENAI_API_KEY
    print("\nHi, I'm your AI Chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=150
        )
        print("Bot:", response.choices[0].text.strip())


# Main function to handle user interaction
def main():
    print("Welcome to the AI Chatbot!")

    encryption_key, users = load_data()

    while True:
        print("\nChoose an option:")
        print("1. Login")
        print("2. Register")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            if authenticate(users):
                chatbot_interaction()  # Call the chatbot interaction function
                break
        elif choice == '2':
            users = register_user(users)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()