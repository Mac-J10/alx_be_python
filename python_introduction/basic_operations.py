# Basic arithmetic operations in Python

def calculate_operations(number1, number2):
    return {
        "addition": number1 + number2,
        "subtraction": number1 - number2,
        "multiplication": number1 * number2,
        }

# Define numbers
number1, number2 = 10, 5

# Get results
results = calculate_operations(number1, number2)

# Display results

print("Addition of", number1, "and", number2, "is", results["addition"])
print("Subtraction of", number1, "and", number2, "is", results["subtraction"])
print("Multiplication of", number1, "and", number2, "is", results["multiplication"])
    
    