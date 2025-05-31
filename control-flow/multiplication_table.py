#Python script named multiplication_table.py.
# then using a for loop to print the multiplication table for that number from 1 to 10.

number = int(input("Enter a number to see its multiplication table:"))
print("\n".join(f"{number} * {i} = {number * i}" for i in range(1, 11)))