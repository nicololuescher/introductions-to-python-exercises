# Develop a function that computes the area of a disc of a given radius.

import math

def getArea(radius):
    return math.pi * radius ** 2

def main():
    print("This program calculates the area of a circle")
    radius = float(input("Enter the radius of the circle: "))
    area = getArea(radius)
    print("The area of the circle is", area)

if(__name__ == "__main__"):
    main()