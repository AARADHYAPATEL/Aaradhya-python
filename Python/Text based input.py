print("Type R to print red colour.")
print("Type B to print blue colour.")
print("Type G to print green colour.")
print("Type Y to print yellow colour.")
n = input("Enter a colour code: ")
if n == 'r' or n == 'R':
    print("You entered red colour.")
elif n == 'b' or n == 'B':
    print("You entered blue colour.")
elif n == 'g' or n == 'G':
    print("You entered green colour.")
elif n == 'y' or n == 'Y':
    print("You entered yellow colour.")
else:
    print("Enter a valid colour code.")
