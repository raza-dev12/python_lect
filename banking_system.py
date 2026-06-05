# import json
import os

# DATA_FILE = "accounts.json"


class BankAccount:
    def __init__(self, acc_no, name, pin, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Successfully deposited ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
            return False

        self.balance -= amount
        print(f"Successfully withdrew ${amount}")
        return True

    def show_balance(self):
        print(f"Current Balance: ${self.balance}")


class Bank:
    def __init__(self):
        self.accounts = self.load_accounts()

    def load_accounts(self):
        if not os.path.exists(DATA_FILE):
            return {}

        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        accounts = {}
        for acc_no, info in data.items():
            accounts[acc_no] = BankAccount(
                acc_no,
                info["name"],
                info["pin"],
                info["balance"]
            )

        return accounts

    def save_accounts(self):
        data = {}

        for acc_no, account in self.accounts.items():
            data[acc_no] = {
                "name": account.name,
                "pin": account.pin,
                "balance": account.balance
            }

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def create_account(self):
        acc_no = input("Enter Account Number: ")

        if acc_no in self.accounts:
            print("Account already exists!")
            return

        name = input("Enter Name: ")
        pin = input("Create 4-digit PIN: ")
        balance = float(input("Initial Deposit: "))

        self.accounts[acc_no] = BankAccount(
            acc_no,
            name,
            pin,
            balance
        )

        self.save_accounts()
        print("Account created successfully!")

    def login(self):
        acc_no = input("Account Number: ")
        pin = input("PIN: ")

        if acc_no not in self.accounts:
            print("Account not found!")
            return None

        account = self.accounts[acc_no]

        if account.pin != pin:
            print("Incorrect PIN!")
            return None

        print(f"\nWelcome {account.name}")
        return account

    def transfer_money(self, sender):
        receiver_acc = input("Receiver Account Number: ")

        if receiver_acc not in self.accounts:
            print("Receiver account not found!")
            return

        amount = float(input("Amount to transfer: "))

        if sender.balance < amount:
            print("Insufficient balance!")
            return

        sender.withdraw(amount)
        self.accounts[receiver_acc].deposit(amount)

        self.save_accounts()

        print("Transfer successful!")

    def account_menu(self, account):
        while True:
            print("\n===== ACCOUNT MENU =====")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transfer Money")
            print("5. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                amount = float(input("Amount: "))
                account.deposit(amount)
                self.save_accounts()

            elif choice == "2":
                amount = float(input("Amount: "))
                account.withdraw(amount)
                self.save_accounts()

            elif choice == "3":
                account.show_balance()

            elif choice == "4":
                self.transfer_money(account)

            elif choice == "5":
                break

            else:
                print("Invalid choice!")

    def main_menu(self):
        while True:
            print("\n===== BANKING SYSTEM =====")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.create_account()

            elif choice == "2":
                account = self.login()

                if account:
                    self.account_menu(account)

            elif choice == "3":
                print("Thank you for using our bank!")
                break

            else:
                print("Invalid choice!")


if __name__ == "__main__":
    bank = Bank()
    bank.main_menu()