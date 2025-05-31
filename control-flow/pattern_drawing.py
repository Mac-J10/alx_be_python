#This script will prompt the user to enter a positive integer, 
# then use nested loops to print a square pattern of that size made of asterisks (*).

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to iterate through each row
while row < size:
    # For loop to print asterisks without newline
    for _ in range(size):
        print("*", end="")
    
    # Print a newline character to move to the next row
    print()
    
    # Increment row counter
    row += 1