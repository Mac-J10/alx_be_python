#Python script named multiplication_table.py.
# then using a for loop to print the multiplication table for that number from 1 to 10.

number = int(input("Enter a number to see its multiplication table: "))
# Using a for loop to print the multiplication table for the given number
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
# This will print the multiplication table for the number entered by the user