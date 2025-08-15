import datetime

class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = int(account_number)
        self.name = name
        self.balance = int(balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount} to account {self.account_number}, name: {self.name}.\nNew Balance: ₹{self.balance}")
        print("======================================")
        with open("transactions.txt", "a", encoding="utf-8") as f:
            f.write(f"Your account {self.account_number}, name: {self.name} has been deposited with ₹{amount} on {datetime.datetime.now()}\n")

    def withdraw(self, amount):
        if amount > self.balance - 500:
            print(f"Insufficient Balance\nYou can't withdraw ₹{amount} from {self.account_number}, name: {self.name}.\nYou can withdraw ₹{self.balance - 500} only")
            print("======================================")
        else:
            self.balance -= amount
            print(f"Your withdrawal is ₹{amount} from {self.account_number}, name: {self.name}.\nNew Balance: ₹{self.balance}")
            print("======================================")
            with open("transactions.txt", "a", encoding="utf-8") as f:
                f.write(f"You have withdrawn ₹{amount} from account {self.account_number}, name: {self.name} on {datetime.datetime.now()}\n")

    def check_balance(self):
        print(f"Your current balance is ₹{self.balance}")
        print("======================================")

    def history(self):
        try:
            with open("transactions.txt", "r", encoding="utf-8") as f:
                content = f.read().strip()
            print("\n=== Transaction History ===")
            if content:
                print(content)
            else:
                print("No transactions found.")
        except FileNotFoundError:
            print("No transaction history file found.")
        print("======================================")



accounts = {}

running = True
while running:
    print("======================================")
    print("BANKING MANAGEMENT SYSTEM")
    print("======================================")

    choice = input("1. Create account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transaction History\n6. Exit\nEnter your choice: ")

    if choice == "1":
        account_number = int(input("Enter your account number: "))
        if account_number in accounts:
            print("Account already exists.")
        else:
            name = input("Enter your name: ")
            balance = int(input("Enter initial balance: "))
            accounts[account_number] = BankAccount(account_number, name, balance)

    elif choice == "2":
        account_number = int(input("Enter your account number: "))
        if account_number not in accounts:
            print("Account does not exist.")
        else:
            amount = int(input("Enter the amount to deposit: "))
            accounts[account_number].deposit(amount)

    elif choice == "3":
        account_number = int(input("Enter your account number: "))
        if account_number not in accounts:
            print("Account does not exist.")
        else:
            amount = int(input("Enter the amount to withdraw: "))
            accounts[account_number].withdraw(amount)

    elif choice == "4":
        account_number = int(input("Enter your account number: "))
        if account_number not in accounts:
            print("Account does not exist.")
        else:
            accounts[account_number].check_balance()

    elif choice == "5":
        account_number = int(input("Enter your account number: "))
        if account_number not in accounts:
            print("Account does not exist.")
        else:
            accounts[account_number].history()

    elif choice == "6":
        print("Exiting the program. Goodbye!")
        print("=========Please visit again=========")
        running = False

    else:
        print("Invalid choice. Please try again.")
