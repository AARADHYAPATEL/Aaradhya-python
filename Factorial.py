num = int(input("Enter a number"))

result = 1

i = 1

while i <= num:
    result *= i
    i += 1

print("The factorial of", num, "is", result)