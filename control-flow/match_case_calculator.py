#Develop a Python script named match_case_calculator.py. 
# This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). 
# The script will then perform the selected operation using a Match Case statement and display the result.

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
                result = "Error: Division by zero is not allowed."
        case _:
            result = "Error: Invalid operation."

    print("The result is:", result)
