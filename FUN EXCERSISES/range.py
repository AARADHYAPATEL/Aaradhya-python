while True:
    amount = int(input("Enter an specific amount"))
    if (amount >= 100 and amount <= 500) or (amount >= 1000 and amount <= 5000):
        print("Amount is between 100 and 500 or amount is between 1000 and 2000.")
    else:
        print("Out of range!")