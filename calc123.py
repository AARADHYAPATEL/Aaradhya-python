def add(n1, n2):
    print("sum = ", n1 + n2)


def subtract(n1, n2):
    print("Result of", n1, "-", n2, "=", (n1 - n2))
    print("Difference = ", abs(n1 - n2))


def multiply(n1, n2):
    print("Product= ", n1 * n2)


def divide(n1, n2):
    if n2 == 0:
        print("Cannot divide by zero")
    else:
        print("Quotient = ", n1 / n2)

        ch2 = int(input("Do you want to find the remainder also? Press 1 for yes and 2 for no."))
        if ch2 == 1:
            print("Remainder = ", n1 % n2)


#def subtract(n1,n2):
#def multiply(n1,n2):
#def divide(n1,n2):

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("0. Exit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        add(n1, n2)
    case 2:
        subtract(n1, n2)
    case 3:
        multiply(n1, n2)
    case 4:
        divide(n1, n2)
    case 0:
        print("Thank you for using the calculator.")
        exit()
    case _:
        print("Invalid choice")
