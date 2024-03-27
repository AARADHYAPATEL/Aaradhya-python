while True:
    ZODIAC = int(input("Enter an year : "))

    if ZODIAC % 12 == 8:
        animal = "Dragon"
    elif ZODIAC % 12 == 9:
        animal = "Snake"
    elif ZODIAC % 12 == 10:
        animal = "Horse"
    elif ZODIAC % 12 == 11:
        animal = "Sheep"
    elif ZODIAC % 12 == 1:
        animal = "Monkey"
    elif ZODIAC % 12 == 2:
        animal = "Rooster"
    elif ZODIAC % 12 == 3:
        animal = "Dog"
    elif ZODIAC % 12 == 4:
        animal = "Pig"
    elif ZODIAC % 12 == 5:
        animal = "Rat"
    elif ZODIAC % 12 == 6:
        animal = "Ox"
    elif ZODIAC % 12 == 7:
        animal = "Tiger"
    elif ZODIAC % 12 == 8:
        animal = "Hare"

    #Report Result
    print("%d is the year of the %s" % (ZODIAC, animal))