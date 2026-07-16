import json
from config import FILENAME
from expense import Expense
 
class ExpenseTracker:
    def __init__(self):
        self.expenses=[]
        self.load()
        

    def add_expense(self,amount,category,description):
        new_id=len(self.expenses)+1
        expense= Expense(new_id,amount,category,description)
        self.expenses.append(expense)
        self.save()

    def view_all(self):
        if not self.expenses:
            print("No expenses found.")
            return
        for expense in self.expenses:
            print(expense)
    
    def delete_expense(self,id):
        self.expenses = [s for s in self.expenses if s.id != id]
        self.save()

    def monthly_report(self, month):
    # filter expenses for that month
        monthly = [e for e in self.expenses if e.date[5:7] == str(month).zfill(2)]
        
        if not monthly:
            print(f"No expenses for month {month}")
            return
        
        # group by category 
        report = {}
        for e in monthly:
            if e.category in report:
                report[e.category] += e.amount
            else:
                report[e.category] = e.amount
        
        print(f"\n--- Monthly Report: Month {month} ---")
        for category, total in report.items():
            print(f"{category}: R{total}")
        print(f"Total: R{sum(report.values())}")


    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f'Total spent: R{total}')


    def save(self):
        data = [{'id': e.id, 'amount': e.amount, 'category': e.category, 'description': e.description, 'date': e.date} for e in self.expenses]
        with open(FILENAME, 'w') as f:
            json.dump(data, f, indent=2)


    def load(self):
        try:
            with open(FILENAME) as f:
                data = json.load(f)
            self.expenses = [Expense(d['id'], d['amount'], d['category'], d['description']) for d in data]
        except FileNotFoundError:
            self.expenses = []
