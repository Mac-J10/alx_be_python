#Python script named multiplication_table.py using a for loop to print the multiplication table for that number from 1 to 10.
# add a print statement for the multiplication table
number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    result = number * i

print(f"{number} x {i} = {result}")

