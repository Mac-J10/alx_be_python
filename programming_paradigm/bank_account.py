class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")


import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 3:
        print("Usage: python main-0.py <initial_balance> <operation> [amount]")
        return

    try:
        initial_balance = float(sys.argv[1])
        operation = sys.argv[2].lower()
        account = BankAccount(initial_balance)

        if operation == "deposit" and len(sys.argv) == 4:
            amount = float(sys.argv[3])
            account.deposit(amount)
            print("Deposit successful.")
        elif operation == "withdraw" and len(sys.argv) == 4:
            amount = float(sys.argv[3])
            if account.withdraw(amount):
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        elif operation == "balance":
            pass  # Just show balance
        else:
            print("Invalid operation or missing amount.")
            return

        account.display_balance()

    except ValueError:
        print("Invalid numeric input.")

if __name__ == "__main__":
    main()