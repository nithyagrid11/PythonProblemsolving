class Repo:
    def __init__(self):
        self.current_id = 1
        self.all_days = {}
    def get_id(self):
        id = self.current_id
        self.current_id += 1
        return id
    def add_expense(self,day,expense):
        if day not in self.all_days:
            self.all_days[day] = []
        self.all_days[day].append(expense)
    def get_expense_day(self,day):
        return self.all_days.get(day, [])
    def get_all_expenses(self):
        return self.all_days
    def delete_expense(self, day, expense_id):
       expenses = self.all_days.get(day, [])
       for expense in expenses:
          if expense['id'] == expense_id:
             expenses.remove(expense)
             return True
       return False
    def update_expense(self,day,expense_id,new_description=None,new_amount=None,new_category=None):
        expenses = self.all_days.get(day,[])
        for expense in expenses:
            if expense['id'] == expense_id:
                if new_description is not None:
                    expense['description'] = new_description
                if new_amount is not None:
                    expense['amount'] = new_amount
                if new_category is not None:
                    expense['category'] = new_category
                return True
        return False

class Analytics:
    @staticmethod
    def total_spent(all_data):
        total = 0
        for day in all_data:
            for expense in all_data[day]:
                total += expense['amount']
        return total
    
    @staticmethod
    def burn_rate(all_data, current_data):
        #burn_rate = total_spent / no_of_days
        total = Analytics.total_spent(all_data)
        if current_data == 0:
            return 0
        return total/current_data
    
    @staticmethod
    def budget_variance(all_data, monthly_budget):
        total = Analytics.total_spent(all_data)
        return monthly_budget - total
    

class ExpenseService:
    def __init__(self,repo, monthly_budget = 10000):
        self.repo = repo
        self.current_day = 1
        self.monthly_budget = monthly_budget

    def add_expense(self, desscription, amount, category):
        all_data = self.repo.get_all_expenses()
        total = Analytics.total_spent(all_data)

        if total + amount > self.monthly_budget:
            print("Budget will be exceeded")
        
        expense_id = self.repo.get_id()

        expense = {
            'id': expense_id,
            'description': desscription,
            'amount': amount,
            'category': category
        }
        self.repo.add_expense(self.current_day,expense)

    def get_today_expense(self):
        return self.repo.get_expense_day(self.current_day)
    
    def get_last_expense(self):
        expenses = self.repo.get_expense_day(self.current_day)
        if not expenses:
            return None
        return expenses[-1]
    
    def end_day(self):
        self.current_day += 1

    def get_burn_rate(self):
       return Analytics.burn_rate(
          self.repo.get_all_expenses(),
          self.current_day
    )

    def get_budget_variance(self):
        return Analytics.budget_variance(
           self.repo.get_all_expenses(),
           self.monthly_budget
    )

    def delete_expense(self, expense_id):
        return self.repo.delete_expense(self.current_day, expense_id)
    
    def update_expense(self, expense_id, new_description=None, new_amount=None, new_category=None):
        updated = self.repo.update_expense(
            self.current_day,
            expense_id,
            new_description,
            new_amount,
            new_category
        )
        if not updated:
            return False

        # Re-check budget after update
        total = Analytics.total_spent(self.repo.get_all_expenses())
        if total > self.monthly_budget:
            print("Warning: Budget exceeded after update!")
        return True

#CLI flow
repo = Repo()
budget = int(input("Enter monthly budget: "))
month = input("Enter the current month: ")
service = ExpenseService(repo, budget)
 
while True:
    print("\n1 -> Add Expense")
    print("2 -> Show Today Expenses")
    print("3 -> Delete Expense")
    print("4 -> Update Expense")
    print("5 -> Burn Rate")
    print("6 -> Budget Variance")
    print("7 -> End Day")
    print("8 -> Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        desc = input("Description: ")
        amount = int(input("Amount: "))
        category = input("Category: ")
        service.add_expense(desc, amount, category)

    elif choice == '2':
        expenses = service.get_today_expense()
        print(expenses)

    elif choice == '3':
        expense_id = int(input("Enter expense ID to delete: "))
        deleted = service.delete_expense(expense_id)
        print("Deleted" if deleted else "Not found")

    elif choice == '4':
        expense_id = int(input("Enter expense ID to update: "))
        new_amount = int(input("New amount: "))
        updated = service.update_expense(expense_id, new_amount=new_amount)
        print("Updated" if updated else "Not found")

    elif choice == '5':
        print("Burn Rate:", service.get_burn_rate())

    elif choice == '6':
        print("Budget Variance:", service.get_budget_variance())

    elif choice == '7':
        service.end_day()
        print("Moved to next day")

    elif choice == '8':
        break

    else:
        print("Invalid choice")
