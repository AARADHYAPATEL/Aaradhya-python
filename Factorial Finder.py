def factorial():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(fact)

def menu():
    print("1. Factorial")
    print("0. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        factorial()
    elif choice == 0:
        print("Thank you for using the Factorial Finder.")
        exit()

menu()