🏦 Banking System Prototype (Python)

Overview

This project is a prototype Banking System built in Python, simulating core banking operations for both bank customers and administrators. The system models a simplified banking environment where users can perform essential financial transactions and account management functions. It is designed as part of an academic assessment to demonstrate a functional banking application.

💡 About the Project

A banking system is a network of financial institutions providing services like handling deposits, processing payments, offering loans, and managing fund transfers. This project focuses on prototyping a core banking solution by simulating operations commonly carried out in real banks.

🎯 Project Objectives

To implement a Python-based banking application.
To allow admins to manage customer accounts (create, update, view, close).
To enable basic banking operations like deposits, withdrawals, balance inquiries, and fund transfers.
To build an extendable system where customer data can be stored either in memory (hard-coded) or externally (e.g., text files for higher marks).


⚙️ Features
✅ Admin Functionalities:

Admin Login system (for secure access).
Create new customer bank accounts.
Search for a specific customer by account number.
View and update customer personal details (name, address, etc.).
Close customer bank accounts.


✅ Banking Operations:

Deposit money into customer accounts.
Withdraw money from customer accounts.
Check account balance.
View customer details (name, address, etc.).

🗄️ Data Handling
The initial version of the system uses hardcoded data for customer records.
To enhance functionality, the system can be upgraded to store customer data in text files (file I/O).

🛠️ Tech Stack
Language: Python 3.x
Paradigm: Object-Oriented Programming (OOP)

Concepts Used: Classes, Functions, File Handling (optional enhancement)


How it Works
Admin logs into the system.
Admin can add or search for customers.
For each customer, basic banking operations like deposit, withdraw, and balance check can be performed.
Admin can also update customer info or close an account.

✨ Enhancement Ideas
Implement file storage for persistent customer data.
Add transaction history logging.
Implement user-side (customer) login for self-service banking.
Add exception handling for robust error management.
