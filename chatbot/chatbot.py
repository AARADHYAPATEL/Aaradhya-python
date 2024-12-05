from cryptography.fernet import Fernet
import json
import bcrypt
import os
import sys
import platform
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# File path for storing user data
USER_DATA_FILE = 'user_data.json'

# Load the DialoGPT model and tokenizer
model_name = "microsoft/DialoGPT-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


# Load or generate encryption key
def load_encryption_key():
    if os.path.exists(USER_DATA_FILE):
        try:
            with open(USER_DATA_FILE, 'r') as file:
                data = json.load(file)
                if 'encryption_key' in data:
                    return data['encryption_key'].encode()
        except (json.JSONDecodeError, KeyError):
            pass
    key = Fernet.generate_key()
    save_user_data({}, key)
    return key


encryption_key = load_encryption_key()





def load_user_data():
    """
        Load user data from a JSON file, decrypt the stored passwords, and return the user data in a readable format.

        This function performs the following steps:
        1. Checks if the user data file exists.
        2. If the file exists, it attempts to read and parse the JSON data.
        3. If the 'users' key is not present in the data, it initializes an empty dictionary for users.
        4. Decrypts the stored passwords using the Fernet encryption key.
        5. Returns the user data as a dictionary with decrypted passwords.
        6. If any errors occur during JSON parsing or key retrieval, it prints an error message and returns an empty dictionary.
        7. If the user data file does not exist, it creates the file with an empty user dictionary and the encryption key, then returns an empty dictionary.

        Returns:
            dict: A dictionary containing usernames as keys and decrypted passwords as values.
    """
    if os.path.exists(USER_DATA_FILE):
        try:
            with open(USER_DATA_FILE, 'r') as file:
                data = json.load(file)
                if 'users' not in data:
                    data['users'] = {}
                fernet = Fernet(encryption_key)
                users = {user: fernet.decrypt(pw.encode()).decode() for user, pw in data['users'].items()}
                return users
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error loading user data: {e}")
            return {}
    else:
        save_user_data({}, encryption_key)
        return {}


def save_user_data(users, key):
    """Save user data to JSON file."""
    fernet = Fernet(key)
    encrypted_users = {user: fernet.encrypt(pw.encode()).decode() for user, pw in users.items()}
    with open(USER_DATA_FILE, 'w') as file:
        json.dump({"encryption_key": key.decode(), "users": encrypted_users}, file, indent=4)


def hash_password(password):
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()


def check_password(password, hashed):
    """Check a password against a bcrypt hashed password."""
    return bcrypt.checkpw(password.encode(), hashed.encode())


def register_user(username, password):
    """Register a new user."""
    users = load_user_data()
    if username in users:
        return "Username already exists."
    hashed_password = hash_password(password)
    users[username] = hashed_password
    save_user_data(users, encryption_key)
    return "User registered successfully."


def login_user(username, password):
    """Log in an existing user."""
    users = load_user_data()
    if username in users and check_password(password, users[username]):
        return "Login successful."
    return "Invalid username or password."


def getpass_with_stars(prompt="Password: "):
    """Prompt for password input with asterisks masking on both Windows and Unix-like systems."""
    if platform.system() == "Windows":
        import msvcrt
        print(prompt, end='', flush=True)
        password = ""
        while True:
            char = msvcrt.getch()
            if char in [b'\r', b'\n']:  # Enter key pressed
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
                if char in ['\r', '\n']:  # Enter key pressed
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


def get_password_confirmation():
    """Prompt the user to enter and confirm their password."""
    while True:
        password = getpass_with_stars("Enter password: ")
        confirm_password = getpass_with_stars("Confirm password: ")
        if password == confirm_password:
            return password
        else:
            print("\nPasswords do not match. Please try again.")


def generate_response(prompt):
    """Generate a response from the DialoGPT model."""
    # Encode the prompt and generate a response
    inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')
    attention_mask = torch.ones(inputs.shape, dtype=torch.long)
    reply_ids = model.generate(inputs, attention_mask=attention_mask, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(reply_ids[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    return response


def chat_interface():
    """Provide a chat interface for the user to interact with the chatbot."""
    print("\n--- ChatBot ---")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("ChatBot: Goodbye!")
            break
        response = generate_response(user_input)
        print(f"ChatBot: {response}")


def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\n--- ChatBot Authentication ---")
        print("1. Register")
        print("2. Login")
        print("3. Chat")
        print("4. Quit")

        choice = input("Choose an option (1/2/3/4): ").strip()

        if choice == '1':
            username = input("Enter username: ").strip()
            password = get_password_confirmation()
            print(register_user(username, password))

        elif choice == '2':
            username = input("Enter username: ").strip()
            password = getpass_with_stars("Enter password: ")
            print(login_user(username, password))

        elif choice == '3':
            print("Please log in to chat.")
            username = input("Enter username: ").strip()
            password = getpass_with_stars("Enter password: ")
            if login_user(username, password) == "Login successful.":
                print("You are now logged in.")
                chat_interface()
            else:
                print("Invalid login. Please try again.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main_menu()