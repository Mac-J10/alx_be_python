from datetime import datetime, timedelta  # Import necessary components

def display_current_datetime():
    """Displays the current date and time in a readable format."""
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    """Calculates and prints the future date based on user input."""
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: ").strip())  # Get user input
        future_date = datetime.now() + timedelta(days=number_of_days)  # Add days
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format it
        print(f"Future Date after {number_of_days} days: {formatted_future_date}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def main():
    """Runs the script with user interaction."""
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()