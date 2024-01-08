def calc():
    dateInput = eval(input("Enter your birth year: "))

    if (dateInput - 1980) % 12 == 0:
        print("You were born in the year of the Monkey")
    elif (dateInput - 1980) % 12 == 1:
        print("You were born in the year of the Rooster")
    elif (dateInput - 1980) % 12 == 2:
        print("You were born in the year of the Dog")
    elif (dateInput - 1980) % 12 == 3:
        print("You were born in the year of the Pig")
    elif (dateInput - 1980) % 12 == 4:
        print("You were born in the year of the Rat")
    elif (dateInput - 1980) % 12 == 5:
        print("You were born in the year of the Ox")
    elif (dateInput - 1980) % 12 == 6:
        print("You were born in the year of the Tiger")
    elif (dateInput - 1980) % 12 == 7:
        print("You were born in the year of the Rabbit")
    elif (dateInput - 1980) % 12 == 8:
        print("You were born in the year of the Dragon")
    elif (dateInput - 1980) % 12 == 9:
        print("You were born in the year of the Snake")
    elif (dateInput - 1980) % 12 == 10:
        print("You were born in the year of the Horse")
    elif (dateInput - 1980) % 12 == 11:
        print("You were born in the year of the Goat")

    else:
        print("This is an invalid input", "\n")
        print(str(calc()))

    return " "


print(calc())
