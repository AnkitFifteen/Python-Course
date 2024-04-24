import Area, Conversion

level_1_options = str(input("What do you want to perform?\n #1 Area Calculation\n #2 Conversion Calculation\nEnter choice number: "))

match level_1_options:
    case "1" | "Area":
        Area.start()
    case "2" | "Conversion":
        Conversion.start()
    case _:
        print("Wrong choice entered.")