import pyfiglet
from termcolor import colored


def wish_happy_easter():
    # Creating a colorful Happy Easter message using pyfiglet and termcolor
    easter_message = pyfiglet.figlet_format("Happy Easter!")
    colored_message = colored(easter_message, color='yellow', attrs=['bold'])

    # additional colorful text
    additional_text = colored("\nWishing you a joyful and blessed Easter !")

    print(colored_message + additional_text)

wish_happy_easter()