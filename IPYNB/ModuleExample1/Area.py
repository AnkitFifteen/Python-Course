import math

def square():
    side = float(input("Enter side of square: "))
    print("Result: ", side ** 2)

def rectangle():
    length = float(input("Enter length of rectangle: "))
    breadth = float(input("Enter breadth of rectangle: "))
    print("Result: ", length * breadth)

def triangle():
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    print("Result: ", (base * height)/2)

def circle():
    radius = float(input("Enter radius of circle: "))
    print("Result: ", math.pi * (radius**2))

def start():
    options = str(input("What do you want to perform?\n #1 Area of Square Calculation\n #2 Area of Rectangle Calculation\n #3 Area of Triangle Calculation\n #4 Area of Circle Calculation\nEnter choice number: "))
    match options:
        case "1":
            square()
        case "2":
            rectangle()
        case "3":
            triangle()
        case "4":
            circle()
        case _: 
            print("Wrong choice entered.")