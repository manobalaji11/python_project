Documentation for the Bank Account Management Project
Introduction
The Bank Account Management Project is a simple Python program that allows users to manage their bank accounts. It provides functionality for creating accounts, viewing balances, depositing money, and withdrawing money. The data is stored and managed using a MySQL database, ensuring the persistence of account information.
This document explains the code and guides you on how to use it effectively.
________________________________________
Features
1.	Account Creation:
o	Allows users to create a new bank account.
o	Requires input for the account holder's name, account type (Savings or Current), and an initial deposit amount.
o	Generates a unique 8-digit account number for each account.
2.	Show Balance:
o	Displays the current balance of the selected account.
3.	Deposit:
o	Allows users to add money to their account.
o	Ensures only positive amounts can be deposited.
4.	Withdraw:
o	Allows users to withdraw money from their account.
o	Prevents withdrawal if the account has insufficient funds or if the amount is negative.
5.	Exit:
o	Terminates the program gracefully.
________________________________________
Prerequisites
Software Requirements
•	Python 3.7 or later
•	MySQL Server
•	MySQL Connector for Python (mysql-connector-python)
Database Setup
The program uses a MySQL database named Bank_management. Before running the program, set up the database as follows:
1.	Create the database:
2.	CREATE DATABASE Bank_management;
3.	Switch to the database:
4.	USE Bank_management;
5.	Create the Accounts table:
6.	CREATE TABLE Accounts (
7.	    account_number INT PRIMARY KEY,
8.	    name VARCHAR(100) NOT NULL,
9.	    account_type ENUM('Savings', 'Current') NOT NULL,
10.	    balance DECIMAL(15, 2) NOT NULL
11.	);
________________________________________
Program Components
1. BankAccount Class
•	Represents a bank account.
•	Attributes: 
o	name: Name of the account holder.
o	account_type: Type of the account (Savings or Current).
o	balance: Current balance in the account.
o	account_number: A unique 8-digit number generated for each account.
•	Methods: 
o	show_balance(): Displays the account balance.
o	deposit(): Adds a specified amount to the account balance and updates the database.
o	withdraw(): Deducts a specified amount from the account balance, provided sufficient funds are available, and updates the database.
2. Account Creation
•	Function: account_creation()
•	Prompts the user for account details and validates the initial deposit amount.
•	Inserts the account details into the Accounts table.
3. Account Selection
•	Function: select_account()
•	Allows users to select an account by entering the account number.
•	Retrieves account details from the database and returns a BankAccount instance.
4. Main Program Flow
•	Function: main()
•	Presents the user with a menu of actions.
•	Processes user input to perform the desired operation.
________________________________________
Usage Instructions
1.	Run the Program:
o	Save the script to a file (e.g., bank_account.py) and run it using Python: 
o	python bank_account.py
2.	Choose an Option:
o	Upon starting the program, a menu will appear with the following options: 
o	1. Account Creation
o	2. Show Balance
o	3. Deposit
o	4. Withdraw
o	5. Exit
3.	Follow Prompts:
o	Enter the required information based on your choice. For example: 
	To create an account, provide the account holder's name, account type, and an initial deposit amount.
	To deposit or withdraw money, select an account by entering its account number.
4.	Exit:
o	Choose option 5 to exit the program.
________________________________________
Error Handling
The program includes error handling for:
•	Invalid inputs (e.g., non-numeric values for deposit/withdrawal amounts).
•	Negative deposit or withdrawal amounts.
•	Insufficient balance during withdrawals.
•	Invalid account numbers.
________________________________________
Future Improvements
1.	Add support for multiple users with login credentials.
2.	Implement additional account operations like transferring funds between accounts.
3.	Create a graphical user interface (GUI) for better usability.
4.	Add transaction history tracking for each account.
________________________________________
Conclusion
The Bank Account Management Project is a beginner-friendly Python program that demonstrates the integration of Python with a MySQL database. It covers fundamental banking operations, making it an excellent learning resource for database-driven application development.

