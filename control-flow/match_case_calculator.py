#Develop a Python script named match_case_calculator.py. 
# This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). 
# The script will then perform the selected operation using a Match Case statement and display the result.
# Ensure to handle the division by zero case gracefully, displaying a message if the user tries to divide by zero.

def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Select an operation (addition, subtraction, multiplication, division): ")

    match operation:
        case "addition":
            result = num1 + num2
        case "subtraction":
            result = num1 - num2
        case "multiplication":
            result = num1 * num2
        case "division":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero."
        case _:
            result = "Error: Invalid operation."

    print("The result is:", result)
