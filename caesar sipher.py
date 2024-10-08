def caesar_sipher(s, shift):
    result = ""
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

print(caesar_sipher("abc", 5))  # bcd