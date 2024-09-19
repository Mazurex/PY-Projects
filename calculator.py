from math import *
from time import sleep

def calc():
    print("----------------------------------------------------------------")
    
    try:
        num1 = float(input("Enter the first number: "))
    except:
        print("Invalid number!")
        calc()

    try:
        num2 = float(input("Enter the second number: "))
    except:
        print("Invalid number!")
        calc()
    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        print(f"The result is: {num1 + num2}")
    elif operation == "-":
        print(f"The result is: {num1 - num2}")
    elif operation == "*":
        print(f"The result is: {num1 * num2}")
    elif operation == "/":
            print(f"The result is: {num1 / num2}")
    else:
        print("Error! Invalid operation")
        calc()
    
    again = input("Would you like to make another calculation (Y/N): ").lower()
    if again == "y":
        calc()

calc()