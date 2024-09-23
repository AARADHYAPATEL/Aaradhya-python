def calculate_taxi_fare(kms):
    fare = 0
    if kms <= 10:
        fare = kms * 25
    elif kms <= 30:
        fare = (10 * 25) + ((kms - 10) * 10)
    elif kms <= 70:
        fare = (10 * 25) + (20 * 10) + ((kms - 30) * 15)
    else:
        fare = (10 * 25) + (20 * 10) + (40 * 15) + ((kms - 70) * 12)
    return fare

def menu():
    import sys
    while True:
        print("1. Calculate Taxi Fare")
        print("2. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                kms = int(input("Enter the distance in kms: "))
                fare = calculate_taxi_fare(kms)
                print("The fare is: ", fare)
            elif choice == 2:
                sys.exit()
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a valid number")

menu()