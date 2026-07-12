# Mini Banking System

class BankAccount:
    def __init__(self, holder_name, account_number, balance):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs. {amount} withdrawn successfully.")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print(f"Current Balance: Rs. {self.balance}")

    def display_account(self):
        print("\n----- Account Details -----")
        print(f"Account Holder : {self.holder_name}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : Rs. {self.balance}")
        print("----------------------------")


# List to store all accounts
accounts = []


# Function to find an account by account number
def find_account(account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None


# Function to create a new account
def create_account():
    name = input("Enter Account Holder Name: ")
    acc_no = input("Enter Account Number: ")
    balance = float(input("Enter Initial Balance: "))

    if find_account(acc_no):
        print("Account number already exists!")
        return

    account = BankAccount(name, acc_no, balance)
    accounts.append(account)
    print("Account created successfully.")


# Function to deposit money
def deposit_money():
    acc_no = input("Enter Account Number: ")
    account = find_account(acc_no)

    if account:
        amount = float(input("Enter Deposit Amount: "))
        account.deposit(amount)
    else:
        print("Account not found.")


# Function to withdraw money
def withdraw_money():
    acc_no = input("Enter Account Number: ")
    account = find_account(acc_no)

    if account:
        amount = float(input("Enter Withdrawal Amount: "))
        account.withdraw(amount)
    else:
        print("Account not found.")


# Function to check balance
def check_balance():
    acc_no = input("Enter Account Number: ")
    account = find_account(acc_no)

    if account:
        account.check_balance()
    else:
        print("Account not found.")


# Function to display all accounts
def display_all_accounts():
    if not accounts:
        print("No accounts available.")
    else:
        for account in accounts:
            account.display_account()


# Main Menu
while True:
    print("\n===== Mini Banking System =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display All Accounts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        display_all_accounts()
    elif choice == "6":
        print("Thank you for using the Mini Banking System!")
        break
    else:
        print("Invalid choice. Please try again.")