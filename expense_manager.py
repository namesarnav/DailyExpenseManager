from collections import defaultdict
import datetime

class ExpenseManager:
    def __init__(self, file_name="expenses.txt"):
        self.file_name = file_name

    def add_transaction(self, date, amount, category):
        with open(self.file_name, "a") as file:
            file.write(f"{date},{amount},{category}\n")

    def get_statistics(self, start_date, end_date):
        expenses = defaultdict(float)
        total_expense = 0
        count = 0

        with open(self.file_name, "r") as file:
            for line in file:
                date, amount, category = line.strip().split(",")
                date = datetime.datetime.strptime(date, "%Y-%m-%d")

                if start_date <= date <= end_date:
                    expenses[category] += float(amount)
                    total_expense += float(amount)
                    count += 1

        return expenses, total_expense, count
