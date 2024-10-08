Str = input("Enter a string: ")
Str = Str.lower()

if Str == Str[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")