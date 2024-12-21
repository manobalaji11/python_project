import random

class BankAccount:
    def __init__(self, name, account_type, initial_deposit):
        self.name = name
        self.account_type = account_type
        self.balance = initial_deposit
        self.account_number = random.randint(10000000, 99999999)

    def show_balance(self):
        print(f"Your balance is: {self.balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("Enter the deposit amount: "))
            if amount < 0:
                print("Invalid amount. Deposit amount must be positive.")
            else:
                self.balance += amount
                print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def withdraw(self):
        try:
            amount = float(input("Enter the withdrawal amount: "))
            if amount > self.balance:
                print("Insufficient balance.")
            elif amount < 0:
                print("Invalid amount. Withdrawal amount must be positive.")
            else:
                self.balance -= amount
                print(f"Withdrawn {amount:.2f}. New balance: {self.balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


accounts = []  # List to store all accounts

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
    accounts.append(account)
    print(f"Account created successfully! Account Number: {account.account_number}")

def select_account():
    try:
        account_number = int(input("Enter account number: "))
        for account in accounts:
            if account.account_number == account_number:
                return account
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
