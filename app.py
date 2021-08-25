"""Calculate the Area of a Circle."""
import math

while True:
    try:
        radius = float(input("Circle Radius: "))
    except ValueError:
        print("Invalid Input: Enter a whole or a decimal number\n")
    else:
        break

area = math.pi * radius**2
print(f"Area: {area}")
