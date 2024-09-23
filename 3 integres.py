a = int(input("Enter a number: "))
b = int(input("Enter a another number: "))
c = int(input("Enter a the third number: "))

def greatest():
    if a > b and a > c:
        print(a, "is the greatest number")
    elif b > a and b > c:
        print(b, "is the greatest number")
    else:
        print(c, "is the greatest number")

def even_or_odd():
    # Check which of the three numbers is even and odd
    if a % 2 == 0:
        print(a, "is even")
    else:
        print(a, "is odd")
    if b % 2 == 0:
        print(b, "is even")
    else:
        print(b, "is odd")
    if c % 2 == 0:
        print(c, "is even")
    else:
        print(c, "is odd")

def sum_and_prod():
    # Calculate the sum and product of the three numbers
    sum = a + b + c
    prod = a * b * c
    print("The sum of the three numbers is", sum)
    print("The product of the three numbers is", prod)

greatest()
even_or_odd()
sum_and_prod()

