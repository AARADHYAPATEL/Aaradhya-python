while True:

    twinkies = int(input("Enter the number of twinkies : "))
    if twinkies < 100 or twinkies > 500:
        print("Too few or too many!")
    else:
        print("Just the right number.")