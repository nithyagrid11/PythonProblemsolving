class Budget_Planning:
    def __init__(self,monthly_budget):
        self.monthly_budget = monthly_budget
        self.year = {}
        self.current_month = 'January'
        self.current_week = 1

    def set_month(self,month):
        Months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        if month not in Months:
            print('Invalid month')
        else:
            self.current_month = month
            if month not in self.year:
                self.year[month] = {}
        self.year['month'] = month

    def get_week(self,week):
        week = self.current_week
        self.current_week += 1
        return week
    
    def add_week(self):
        week_no = self.current_week
        self.year[self.current_month][f"Week {week_no}"] = {}
        self.current_week += 1
    
    def add_categories(self):
        category = {"Rapido": 625, "Biryani": 125, "Snacks": 700, "Fruits": 200, "Essentials": 800, "Other":2000}
        week_key = f"Week {self.current_week - 1}"
        self.year[self.current_month][week_key] = category

    #calculations



monthly_budget = int(input("Enter the budget of this month: "))


