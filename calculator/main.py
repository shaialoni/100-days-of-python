#Calculator app
from art import logo

#Add
def add(n1, n2):
    """Takes two numbers and returns their sum"""
    return n1 + n2

#Subtract
def subtract(n1, n2):
    """Takes two numbers and returns the result of subtracting the second from the first"""
    return n1 - n2

#Multiply
def multiply(n1, n2):
    """Takes two numbers and returns the result of multiplying them"""
    return n1 * n2

#Divide
def divide(n1, n2):
    """Takes two numbers and returns the result of dividing the first in the second"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    keep_calculating = True
    answer = 0

    num1 = float(input("What is the first number?: "))
    for symbol in operations:
            print(symbol)

    while keep_calculating:
        operation_symbol = input("Pick an operation from the lines above: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ").lower() == "y":
            num1 = answer
        else:
            keep_calculating = False
            calculator()

calculator()