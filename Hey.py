Factorial = int(input("Enter a number: "))


def factorial(Factorial):
    if Factorial == 0:
        return 1
    else:
        return Factorial * factorial(Factorial - 1)


print(factorial(Factorial))
