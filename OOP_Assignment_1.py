#!/usr/bin/python3

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds!")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, transaction_limit):
        super().__init__(account_number, balance)
        self.transaction_limit = transaction_limit

    def withdraw(self, amount):
        if amount <= self.transaction_limit:
            super().withdraw(amount)
        else:
            print("Transaction Limit Exceeded!")

class BusinessAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            super().withdraw(amount)
        else:
            print("Withdrawal Amount Exceeds Overdraft Limit!")

def create_account():
    account_type = input("Enter account type\n1 - Savings\n2 - Checking\n3 - Business:\n")
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))

    if account_type == "1":
        interest_rate = float(input("Enter interest rate: "))
        account = SavingsAccount(account_number, initial_balance, interest_rate)
    elif account_type == "2":
        transaction_limit = float(input("Enter transaction limit: "))
        account = CheckingAccount(account_number, initial_balance, transaction_limit)
    elif account_type == "3":
        overdraft_limit = float(input("Enter overdraft limit: "))
        account = BusinessAccount(account_number, initial_balance, overdraft_limit)
    else:
        print("Invalid Account Type!")
        return

    accounts.append(account)
    print("Account Created Successfully")

def perform_transaction(account):
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter the amount you wish to deposit: "))
        account.deposit(amount)
        print("Deposit successful")
    elif choice == "2":
        amount = float(input("Enter the amount you wish to withdraw: "))
        account.withdraw(amount)
    elif choice == "3":
        balance = account.get_balance()
        print("Your current balance is:", balance)
    else:
        print("Invalid choice!")

def main_menu():
    print("\n***** Banking System *****")
    print("1. Create Account")
    print("2. Perform Transaction")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        account_number = input("Enter your account number: ")
        account = None

        for acc in accounts:
            if acc.account_number == account_number:
                account = acc
                break

        if account is not None:
            perform_transaction(account)
        else:
            print("Account not found!")
    elif choice == "3":
        print("***** Exiting the Program *****")
        exit()
    else:
        print("Invalid choice!")


# List to store created account
accounts = []

while True:
    main_menu()
