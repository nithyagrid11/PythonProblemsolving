class Repo:
    def __init__(self):
        self.current_id = 1
        self.month = ""
        self.data = {}
    def get_month(self,month):
        if month not in self.data:
            self.data[month] = {}
        
    def get_id(self):
        day = self.current_id
        self.current_id += 1
        return day
    def add_expense(self,month,day,expense):
        month = Repo.get_month()
        if day not in self.data:
            self.data[month][day] = []
        self.data[month][day].append(expense)
    def get_expense_per_day(self,month,day):
        return self.data.get(month,{}).get(day,[])
    def get_total_expense(self):
        return self.data

class Service:
    def __init__(self,repo):
        self.repo = repo
        self.current_id = 1
        self.current_month = repo.get_month()
    def add_expense(self,desc,amount,category):
        expense = {
            'day': self.current_id,
            'description': desc,
            'amount': amount,
            'category': category
        }
        self.repo.add_expense(self.current_month,self.current_id,expense)
    
repo = Repo()