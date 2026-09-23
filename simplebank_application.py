import json

# ============================================================
# LOAD EXISTING ACCOUNT DATA
# ============================================================

try:
    with open("Accounts_data.json", "r") as file:
        accounts = json.load(file)

except FileNotFoundError:
    print("Accounts_data.json file does not exist. Creating a new one...")
    accounts = {}

except json.JSONDecodeError:
    print("JSON file is empty or corrupted. Starting with empty accounts.")
    accounts = {}


# ============================================================
# DISPLAY MENU
# ============================================================

def display_menu():
    print("\n####========= Banking Management System =========####")
    print("1. Create Account")
    print("2. View Account Details")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Bank Balance")
    print("6. Exit")


# ============================================================
# SAVE DATA INTO JSON FILE
# ============================================================

def save_accounts():
    with open("Accounts_data.json", "w") as file:
        json.dump(accounts, file, indent=4)


# ============================================================
# CREATE ACCOUNT
# ============================================================

def create_account():

    try:
        account_holder = input("Enter the account holder name: ")
        account_number = input("Enter your account number: ")
        age = int(input("Enter your current age: "))
        balance = float(input("Enter your bank balance: "))

        # Validation
        if len(account_number) != 12:
            print("Invalid account number. Please enter exactly 12 digits.")

        elif not account_number.isdigit():
            print("Account number must contain only digits.")

        elif age < 8:
            print("Invalid user age. Age must be 8 or above.")

        elif balance < 0:
            print("Invalid bank balance. Balance cannot be negative.")

        elif account_number in accounts:
            print("This account already exists!")

        else:
            accounts[account_number] = {
                "Account_Holder": account_holder,
                "Account_Number": account_number,
                "Age": age,
                "Balance": balance
            }

            save_accounts()

            print("Account added successfully!")


    except (ValueError, TypeError):
        print("Invalid details. Please check the entered details.")


# ============================================================
# VIEW ACCOUNT DETAILS
# ============================================================

def display_details():

    if not accounts:
        print("No accounts exist.")
    else:
        for account_number, details in accounts.items():

            print("\n--------------------------------")
            print("Account Number :", account_number)
            print("Account Holder :", details["Account_Holder"])
            print("Age            :", details["Age"])
            print("Balance        :", details["Balance"])
            print("--------------------------------")

        print("Account details displayed successfully!")


# ============================================================
# DEPOSIT MONEY
# ============================================================

def deposit_amount():

    try:
        acc_number = input("Enter your account number: ")
        amount = float(input("Enter your deposit amount: "))

        if acc_number not in accounts:
            print("Invalid account number. Account does not exist.")

        elif amount <= 0:
            print("Invalid amount. Please enter a positive amount.")

        else:
            accounts[acc_number]["Balance"] += amount

            save_accounts()

            print("Amount deposited successfully!")
            print("Current Balance:", accounts[acc_number]["Balance"])


    except (ValueError, TypeError):
        print("Something went wrong. Please try again.")


# ============================================================
# WITHDRAW MONEY
# ============================================================

def withdraw_amount():

    try:
        acc_number = input("Enter your account number: ")
        amount = float(input("Enter your withdrawal amount: "))

        if acc_number not in accounts:
            print("Invalid account number. Account does not exist.")

        elif amount <= 0:
            print("Invalid amount. Please enter a positive amount.")

        elif accounts[acc_number]["Balance"] < amount:
            print("Insufficient bank balance.")

        else:
            accounts[acc_number]["Balance"] -= amount

            save_accounts()

            print("Amount withdrawn successfully!")
            print("Current Balance:", accounts[acc_number]["Balance"])


    except (ValueError, TypeError):
        print("Something went wrong. Please try again.")


# ============================================================
# CHECK BANK BALANCE
# ============================================================

def check_balance():

    acc_number = input("Enter your account number: ")

    if acc_number not in accounts:
        print("Invalid account number. Account does not exist.")

    else:
        balance = accounts[acc_number]["Balance"]

        print("Account Holder:", accounts[acc_number]["Account_Holder"])
        print("Current Balance:", balance)


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():

    while True:

        display_menu()

        try:
            option = int(input("Enter your option (1/2/3/4/5/6): "))

            if option == 1:
                create_account()

            elif option == 2:
                display_details()

            elif option == 3:
                deposit_amount()

            elif option == 4:
                withdraw_amount()

            elif option == 5:
                check_balance()

            elif option == 6:
                print("Thank you for using the Banking Management System!")
                break

            else:
                print("Invalid option. Please select 1 to 6.")

        except ValueError:
            print("Please enter a valid number.")


# ============================================================
# PROGRAM START
# ============================================================

main()
