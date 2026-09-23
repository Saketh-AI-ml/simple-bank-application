# 🏦 Simple Bank Management System

A simple **Bank Management System built using Python** that allows users to create bank accounts, view account details, deposit money, withdraw money, and check their account balance.

The application uses **JSON file handling** to store account information locally, so the data can be loaded again when the application is restarted.

---

## 📌 Features

* Create a new bank account
* Validate account details
* View account details
* Deposit money
* Withdraw money
* Check current bank balance
* Prevent withdrawal when the balance is insufficient
* Store account data using JSON
* Load existing account data when the application starts
* Handle invalid user input using exception handling
* Persistent local data storage

---

## 🛠️ Technologies Used

* **Python**
* **JSON**
* **File Handling**
* **Exception Handling**
* **Dictionaries**
* **Functions**
* **Loops**
* **Conditional Statements**

---

## 📂 Project Structure

```text
simple-bank-application/
│
├── simplebank_application.py
├── README.md
└── .gitignore
```

> `Accounts_data.json` is used for local data storage and is excluded from GitHub using `.gitignore`.

---

## ⚙️ How It Works

When the application starts, it checks whether the account data file exists.

If the file exists:

```text
Accounts_data.json
        ↓
     Load Data
        ↓
     accounts
```

If the file does not exist, an empty account dictionary is created.

The user can then select an option from the banking menu.

```text
1. Create Account
2. View Account Details
3. Deposit Money
4. Withdraw Money
5. Check Bank Balance
6. Exit
```

Whenever an account is created, money is deposited, or money is withdrawn, the updated account information is saved to the JSON file.

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/simple-bank-application.git
```

### 2. Navigate to the project directory

```bash
cd simple-bank-application
```

### 3. Run the Python application

```bash
python simplebank_application.py
```

---

## 💡 Example

### Create Account

```text
Enter the account holder name: Saketh
Enter your account number: 123456789012
Enter your current age: 21
Enter your bank balance: 5000

Account added successfully!
```

### Deposit Money

```text
Enter your account number: 123456789012
Enter your deposit amount: 2000

Amount deposited successfully!
Current Balance: 7000
```

### Withdraw Money

```text
Enter your account number: 123456789012
Enter your withdrawal amount: 1000

Amount withdrawn successfully!
Current Balance: 6000
```

---

## 🔐 Data Storage

The project uses Python's built-in `json` module to store account information.

Example structure:

```json
{
    "123456789012": {
        "Account_Holder": "Saketh",
        "Account_Number": "123456789012",
        "Age": 21,
        "Balance": 6000
    }
}
```

For security reasons, actual account or personal information should **never be uploaded to GitHub**.

---

## 🎯 Learning Objectives

This project was built to practice and strengthen fundamental Python programming concepts, including:

* Functions
* Dictionaries
* Loops
* Conditional logic
* Exception handling
* File handling
* JSON serialization and deserialization
* Modular program structure
* Basic data persistence
* Git and GitHub workflow

---

## 🔮 Future Improvements

Possible future improvements include:

* Transaction history
* PIN/password authentication
* Multiple user roles
* Transfer money between accounts
* Delete account
* Update account details
* Transaction timestamps
* SQLite/MySQL database integration
* Object-Oriented Programming implementation
* GUI using Tkinter
* Web application using Flask or FastAPI

---

## 👨‍💻 Author

**Saketh Reddy**

This project was created as part of my Python programming practice and project-based learning journey.

---

## 📄 License

This project is created for educational and learning purposes.
