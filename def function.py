String = input("Enter a string: ")


def is_palindrome(String):
    String = String.lower().replace(" ", "")
    return String == String[::-1]


print(is_palindrome(String))
