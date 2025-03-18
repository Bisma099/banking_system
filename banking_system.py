import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# Admin Info
admin_info = {"username": "admin", "password": "password"}

# Customer Data File
DATA_FILE = "customers.json"
customers = {}

# Load Customer Data
def load_customers():
    global customers
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            customers = json.load(file)

# Save Customer Data
def save_customers():
    with open(DATA_FILE, "w") as file:
        json.dump(customers, file, indent=4)

# ---------------- Main Menu ---------------- #
def main_menu(status_label):
    window = tk.Tk()
    window.title("Banking System")
    window.geometry("400x500")
    window.config(bg="black")

    # Helper function to create buttons
    def create_button(text, command):
        return tk.Button(window, text=text, command=command, bg="white", fg="black", width=30, height=2)

    # Buttons for the main menu
    create_button("Create Customer Account", lambda: create_customer(status_label)).pack(pady=5)
    create_button("View Customer Details", lambda: view_customer(status_label)).pack(pady=5)
    create_button("Deposit Money", lambda: deposit_money(status_label)).pack(pady=5)
    create_button("Withdraw Money", lambda: withdraw_money(status_label)).pack(pady=5)
    create_button("Delete Customer Account", lambda: delete_customer(status_label)).pack(pady=5)
    create_button("Management Report", lambda: management_report(status_label)).pack(pady=5)

    # Exit Button
    tk.Button(window, text="Exit", command=window.destroy, bg="black", fg="black", width=30, height=2).pack(pady=10)

    window.mainloop()

# ---------------- GUI Functions ---------------- #

# Show success message in status label
def show_success(status_label, message):
    status_label.config(text=message, fg="green")

# Show error message in status label
def show_error(status_label, message):
    status_label.config(text=message, fg="red")

# Admin Login Function
def admin_login(status_label):
    username = username_entry.get()
    password = password_entry.get()
    if username == admin_info['username'] and password == admin_info['password']:
        login_window.destroy()
        main_menu(status_label)
    else:
        show_error(status_label, "Invalid credentials!")

# Create Customer Account
def create_customer(status_label):
    account_number = simpledialog.askstring("Account Creation", "Enter account number:")
    if account_number in customers:
        show_error(status_label, "Account already exists!")
        return

    name = simpledialog.askstring("Account Creation", "Enter customer name:")
    address = simpledialog.askstring("Account Creation", "Enter customer address:")
    balance = float(simpledialog.askstring("Account Creation", "Enter initial deposit amount:"))
    account_type = simpledialog.askstring("Account Creation", "Enter account type (Savings/Business):").capitalize()
    interest_rate = float(simpledialog.askstring("Account Creation", "Enter interest rate (%):"))
    overdraft_limit = float(simpledialog.askstring("Account Creation", "Enter overdraft limit:"))

    customers[account_number] = {
        "name": name,
        "address": address,
        "balance": balance,
        "account_type": account_type,
        "interest_rate": interest_rate,
        "overdraft_limit": overdraft_limit
    }
    save_customers()
    show_success(status_label, f"Account for {name} created successfully!")

# View Customer Details
def view_customer(status_label):
    account_number = simpledialog.askstring("View Customer", "Enter account number:")
    if account_number in customers:
        customer = customers[account_number]
        details = (f"Name: {customer['name']}\n"
                   f"Address: {customer['address']}\n"
                   f"Balance: {customer['balance']}\n"
                   f"Account Type: {customer['account_type']}\n"
                   f"Interest Rate: {customer['interest_rate']}%\n"
                   f"Overdraft Limit: {customer['overdraft_limit']}")
        messagebox.showinfo("Customer Details", details)
    else:
        show_error(status_label, "Account not found!")

# Deposit Money
def deposit_money(status_label):
    account_number = simpledialog.askstring("Deposit", "Enter account number:")
    if account_number in customers:
        amount = simpledialog.askstring("Deposit", "Enter amount to deposit:")
        if amount is not None:
            try:
                amount = float(amount)
                customers[account_number]['balance'] += amount
                save_customers()
                messagebox.showinfo("Deposit Successful", f"Deposited {amount} successfully.")
            except ValueError:
                show_error(status_label, "Invalid deposit amount!")
        else:
            show_error(status_label, "Deposit canceled!")
    else:
        show_error(status_label, "Account not found!")

# Withdraw Money
def withdraw_money(status_label):
    account_number = simpledialog.askstring("Withdraw", "Enter account number:")
    if account_number in customers:
        amount = simpledialog.askstring("Withdraw", "Enter amount to withdraw:")
        if amount is not None:
            try:
                amount = float(amount)
                if amount <= customers[account_number]['balance'] + customers[account_number]['overdraft_limit']:
                    customers[account_number]['balance'] -= amount
                    save_customers()
                    messagebox.showinfo("Withdrawal Successful", f"Withdrawn {amount} successfully.")
                else:
                    show_error(status_label, "Insufficient funds or overdraft limit reached!")
            except ValueError:
                show_error(status_label, "Invalid withdrawal amount!")
        else:
            show_error(status_label, "Withdrawal canceled!")
    else:
        show_error(status_label, "Account not found!")

# Delete Customer Account
def delete_customer(status_label):
    account_number = simpledialog.askstring("Delete", "Enter account number to delete:")
    if account_number in customers:
        del customers[account_number]
        save_customers()
        messagebox.showinfo("Customer Deleted", "Customer account deleted successfully!")
    else:
        show_error(status_label, "Account not found!")

# Management Report
def management_report(status_label):
    total_customers = len(customers)
    total_balance = sum(c['balance'] for c in customers.values())
    total_interest = sum(c['balance'] * c['interest_rate'] / 100 for c in customers.values())
    total_overdraft = sum(c['overdraft_limit'] for c in customers.values())

    report = (f"Total Customers: {total_customers}\n"
              f"Total Balance: {total_balance}\n"
              f"Total Interest Payable: {total_interest}\n"
              f"Total Overdraft Limit: {total_overdraft}")
    messagebox.showinfo("Management Report", report)

# ---------------- Login Window ---------------- #
def login_window_setup():
    global login_window, username_entry, password_entry, status_label
    login_window = tk.Tk()
    login_window.title("Admin Login")
    login_window.geometry("300x200")
    login_window.config(bg="black")

    tk.Label(login_window, text="Username", bg="black", fg="white").pack(pady=5)
    username_entry = tk.Entry(login_window, bg="white", fg="black")
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Password", bg="black", fg="white").pack(pady=5)
    password_entry = tk.Entry(login_window, show="*", bg="white", fg="black")
    password_entry.pack(pady=5)

    status_label = tk.Label(login_window, text="", fg="red", bg="black")
    status_label.pack(pady=5)

    tk.Button(login_window, text="Login", command=lambda: admin_login(status_label), bg="white", fg="black").pack(pady=10)

    login_window.mainloop()

# Initial Setup
if __name__ == "__main__":
    load_customers()
    login_window_setup()
