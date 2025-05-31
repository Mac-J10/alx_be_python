#Python script named multiplication_table.py using a for loop to print the multiplication table for that number from 1 to 10.

def print_multiplication_table():
    number = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    print_multiplication_table()