# Simple Calculator
"""
Title: Simple Calculator
Description: A calculator program that performs basic arithmetic operations: addition, subtraction, multiplication, and division. The user inputs two numbers and an operator, and the result of the operation is displayed. The program continues until the user decides to exit.
"""
def calculator():
    """
    Function: calculator
    Description: Implements a simple calculator with support for basic arithmetic operations.
    """
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator: ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            print(f"Result: {num1 + num2}")
        elif operator == '-':
            print(f"Result: {num1 - num2}")
        elif operator == '*':
            print(f"Result: {num1 * num2}")
        elif operator == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Cannot divide by zero.")
        else:
            print("Invalid operator.")

        if input("Do you want to calculate again? (yes/no): ").lower() != 'yes':
            break

calculator()