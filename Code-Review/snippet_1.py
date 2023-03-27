import math

//  Calculate the area of a circle with the given radius.
def calculateArea(radius):
    return math.pi * radius ** 2

// Divide two numbers and return their quotient.

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero"
