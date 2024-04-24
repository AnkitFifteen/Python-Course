def cm_to_meter():
    cm = float(input("Enter cm: "))
    print(cm + " centimetres in metres is: ", cm/100)

def inch_to_cm():
    inch = float(input("Enter inch: "))
    print(inch + " inch in centimetres is: ", inch * 2.54)

def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter fahrenheit: "))
    print(fahrenheit + " fahrenheit in celsius is: ", (fahrenheit- 32) * 5/9)

def start():
    options = str(input("What do you want to perform?\n #1 Centimetre to Meter Calculation\n #2 Inch to Centimetre Calculation\n #3 Fahrenheit to Celsius Calculation\nEnter choice number: "))
    match options:
        case "1":
            cm_to_meter()
        case "2":
            inch_to_cm()
        case "3":
            fahrenheit_to_celsius()
        case _:
            print("Wrong choice entered.")
            