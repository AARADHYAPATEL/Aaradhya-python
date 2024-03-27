while True:
    colour = int(input("Enter an wavelength : "))
    if colour >= 380 and colour < 450:
        c = 'Voilet'
    elif colour >= 450 and colour < 495:
        c = 'Blue'
    elif colour >= 495 and colour < 570:
        c = 'Green'
    elif colour >= 570 and colour < 590:
        c = 'Yellow'
    elif colour >= 590 and colour < 620:
        c = 'Orange'
    elif colour > 620 and colour == 750:
        c = 'Red'
    else:
        c = ""

    if c == "":
        print("That wasn't a valid wavelength.")
    else:
        print("The colour for %s wavelength is %s colour" % (colour, c))
