import tkinter as tk
from tkinter import messagebox
from expense_manager import ExpenseManager
import datetime

class ExpenseManagerGUI:
    def __init__(self, expense_manager):
        self.expense_manager = expense_manager
        self.create_gui()

    def create_gui(self):
        self.root = tk.Tk()
        root.title("Daily Expense Manager")

# Input transaction
        label_input = tk.Label(root, text="Input transaction")
        label_input.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        label_date = tk.Label(root, text="Date (YYYY-MM-DD):")
        label_date.grid(row=1, column=0, padx=10, pady=10, sticky="E")
        entry_date = tk.Entry(root)
        entry_date.grid(row=1, column=1, padx=10, pady=10)

        label_amount = tk.Label(root, text="Amount:")
        label_amount.grid(row=2, column=0, padx=10, pady=10, sticky="E")
        entry_amount = tk.Entry(root)
        entry_amount.grid(row=2, column=1, padx=10, pady=10)

        label_category = tk.Label(root, text="Category:")
        label_category.grid(row=3, column=0, padx=10, pady=10, sticky="E")
        entry_category = tk.Entry(root)
        entry_category.grid(row=3, column=1, padx=10, pady=10)

        button_add_transaction = tk.Button(root, text="Add transaction", command=add_transaction)
        button_add_transaction.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # ... (create all GUI elements as before)
        # ... (define add_transaction and show_statistics functions as before)

    def run(self):
        self.root.mainloop()
        
    def add_transaction(self):
        # ... (code to get user input)
        self.expense_manager.add_transaction(date, amount, category)
        messagebox.showinfo("Success", "Transaction added successfully!")

    def show_statistics(self):
        # ... (code to get user input)
        expenses, total_expense, count = self.expense_manager.get_statistics(start_date, end_date)
        # ... (code to display statistics)
