# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """User interaction for temperature conversion."""
    try:
        temp_value = float(input("Enter the temperature to convert: ").strip())  # Validate numeric input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "F":
            converted_temp = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted_temp:.2f}°C")
        elif unit == "C":
            converted_temp = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted_temp:.2f}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()