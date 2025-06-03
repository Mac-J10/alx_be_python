  # arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """Performs basic arithmetic operations based on the given operation."""
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."

print(perform_operation(10, 5, "add"))  # Example usage
print(perform_operation(10, 5, "subtract"))
print(perform_operation(10, 5, "multiply"))
print(perform_operation(10, 5, "divide"))
print(perform_operation(10, 0, "divide"))
print(perform_operation(10, 5, "invalid"))

