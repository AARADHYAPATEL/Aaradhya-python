# Outer loop for each line
for i in range(1, 200):
    # Inner loop to print stars on each line
    for j in range(i):
        print('*', end='')  # Print star without newline
    print()  # Print newline after each line of stars
