while True:
    A = 4.0
    A_MINUS = 3.7
    B_PLUS = 3.3
    B = 3.0
    B_MINUS = 2.7
    C_PLUS = 2.3
    C = 2.0
    C_MINUS = 1.7
    D_PLUS = 1.3
    D = 1.0
    F = 0
    INVALID = -1

    letter = input("Enter an letter : ")
    letter = letter.upper()

    if letter == 'A+' or letter == 'A':
        gp = A
    elif letter == 'A-':
        gp = A_MINUS
    elif letter == 'B+':
        gp = B_PLUS
    elif letter == 'B':
        gp = B
    elif letter == 'B-':
        gp = B_MINUS
    elif letter == 'C+':
        gp = C_PLUS
    elif letter == 'C':
        gp = C
    elif letter == 'C-':
        gp = C_MINUS
    elif letter == 'D+':
        gp = D_PLUS
    elif letter == 'D':
        gp = D
    elif letter == 'F':
        gp = F
    else:
        gp = INVALID

    #Display the output
    if gp == INVALID:
        print("That wasn't a valid number of grade points.")
    else:
        print("Thats", gp, "Grade pints")
