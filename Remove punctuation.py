def remove_punctuation(s):
    return ''.join([c for c in s if c.isalnum() or c.isspace()])

print(remove_punctuation("Hello, World!"))  # Hello World