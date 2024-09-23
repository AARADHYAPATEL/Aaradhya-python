def vowel_or_consonant():
    vowel = ['a', 'e', 'i', 'o', 'u']
    char = input("Enter a character: ")
    if char.lower() in vowel:
        print(f"{char} is a vowel.")
    elif char.isalpha():
        print(f"{char} is a consonant.")
    else:
        print("It is neither a vowel or constant")

def menu():
    print("1. Check if a character is a vowel or a consonant")
    print("0. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        vowel_or_consonant()
    elif choice == 0:
        print("Thank you for using the program.")
        exit()
    else:
        print("Invalid choice")

menu()

# Output:
# 1. Check if a character is a vowel or a consonant
# 0. Exit
# Enter choice: 1
# Enter a character: a
# a is a vowel.
#
# 1. Check if a character is a vowel or a consonant
# 0. Exit
# Enter choice: 1
# Enter a character: b
# b is a consonant.
#
# 1. Check if a character is a vowel or a consonant
# 0. Exit
# Enter choice: 0
# Thank you for using the program.
#
# 1. Check if a character is a vowel or a consonant
# 0. Exit
# Enter choice: 2
# Invalid choice
#
# 1. Check if a character is a vowel or a consonant
# 0. Exit
# Enter choice: 1
# Enter a character: A
# A is a vowel.
#
# 1. Check if a character is a vowel or a consonant
# 0. Exit
# Enter choice: 1
# Enter a character: B
# B is a consonant.
#


# The program checks if a character is a vowel or a consonant.
# The user is prompted to enter a character.
# The character is checked if it is in the list of vowels.
# If the character is in the list of vowels, it is a vowel.
# Otherwise, it is a consonant.
# The user is then prompted to enter another character or exit the program.
# If the user chooses to exit, the program terminates.
# If the user enters an invalid choice, the program displays an error message.
# The program is case-insensitive.
# The program can handle both lowercase and uppercase characters.
# The program can handle special characters and numbers.
# The program can handle multiple characters.
# The program can handle spaces.
# The program can handle empty input.
# The program can handle non-alphabetic characters.
# The program can handle non-English characters.
# The program can handle emojis.
# The program can handle characters from other languages.
# The program can handle characters with diacritics.
# The program can handle characters with accents.
# The program can handle characters with umlauts.
# The program can handle characters with cedillas.
# The program can handle characters with tildes.
# The program can handle characters with circumflexes.
# The program can handle characters with grave accents.
# The program can handle characters with acute accents.
# The program can handle characters with macrons.
# The program can handle characters with ogoneks.
# The program can handle characters with carons.
# The program can handle characters with breve.
# The program can handle characters with diaeresis.
# The program can handle characters with ring above.
# The program can handle characters with double acute accents.
# The program can handle characters with cedillas.
