import random
import mysql.connector
from decimal import Decimal

# Database connection
db = mysql.connector.connect(
    host="localhost",
    port=3306,  # Explicitly set the port if necessary
    user="root",
    password="Tiger",
    database="Bank_manegement"
)

cursor = db.cursor()


class BankAccount:
    def __init__(self, name, account_type, balance, account_number=None):
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.account_number = account_number or random.randint(10000000, 99999999)

    def show_balance(self):
        print(f"Your balance is: {self.balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("Enter the deposit amount: "))
            if amount < 0:
                print("Invalid amount. Deposit amount must be positive.")
            else:
                self.balance += Decimal(amount)  # Convert amount to Decimal
                cursor.execute(
                    "UPDATE Accounts SET balance = %s WHERE account_number = %s",
                    (self.balance, self.account_number),
                )
                db.commit()
                print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def withdraw(self):
        try:
            amount = float(input("Enter the withdrawal amount: "))
            if amount > float(self.balance):  # Convert balance to float for comparison
                print("Insufficient balance.")
            elif amount < 0:
                print("Invalid amount. Withdrawal amount must be positive.")
            else:
                self.balance -= Decimal(amount)  # Convert amount to Decimal
                cursor.execute(
                    "UPDATE Accounts SET balance = %s WHERE account_number = %s",
                    (self.balance, self.account_number),
                )
                db.commit()
                print(f"Withdrawn {amount:.2f}. New balance: {self.balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def account_creation():
    name = input("Enter account holder's name: ")
    account_type = input("Enter account type (Savings/Current): ")
    try:
        initial_deposit = float(input("Enter initial deposit amount: "))
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return
    except ValueError:
        print("Invalid input for initial deposit. Please enter a number.")
        return

    account = BankAccount(name, account_type, initial_deposit)
    cursor.execute("INSERT INTO Accounts (account_number, name, account_type, balance) VALUES (%s, %s, %s, %s)",
                   (account.account_number, account.name, account.account_type, account.balance))
    db.commit()
    print(f"Account created successfully! Account Number: {account.account_number}")


def select_account():
    try:
        account_number = int(input("Enter account number: "))
        cursor.execute("SELECT * FROM Accounts WHERE account_number = %s", (account_number,))
        result = cursor.fetchone()
        if result:
            return BankAccount(result[1], result[2], result[3], result[0])
        print("Account not found.")
        return None
    except ValueError:
        print("Invalid account number.")
        return None


def main():
    is_running = True

    while is_running:
        print("\nBanking Program")
        print("1. Account Creation")
        print("2. Show Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            account_creation()
        elif choice == '2':
            account = select_account()
            if account:
                account.show_balance()
        elif choice == '3':
            account = select_account()
            if account:
                account.deposit()
        elif choice == '4':
            account = select_account()
            if account:
                account.withdraw()
        elif choice == '5':
            is_running = False
        else:
            print("That is not a valid choice.")

    print("Thank you! Have a nice day!")


if __name__ == '__main__':
    main()
