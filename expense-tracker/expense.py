import datetime
datetime.date.today()

class Expense:
    def __init__(self,id,amount,category,description=""):
        self.amount=amount
        self.category=category
        self.description=description
        self.date=str(datetime.date.today())
        self.id=id
    
    def __str__(self):
        return f'ID: {self.id} | {self.date} | {self.category} | R{self.amount} | {self.description}'

