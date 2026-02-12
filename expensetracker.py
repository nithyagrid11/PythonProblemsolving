class Tracker:
    
    def __init__(self):
        self.all_days = {1: [], 2: [], 3: []}
        self.current_day = 1
        self.next_id = 1

    #func taking i/p values and appending to all_days dictionary
    def expense_func(self,description,amount):
        if self.current_day > 3:
            print("Tracker completed. No more entries allowed.")
            print('warning')
            exit
        
        id = self.next_id
        one_expense = {'id': id, 'description': description, 'amount': amount}
        self.all_days[self.current_day].append(one_expense)
        self.next_id += 1
    
    #displaying todays expenses and also total expenses
    def display_today_expenses(self):
        total = 0
        today_expenses = self.all_days[self.current_day]
        if not today_expenses:   #today_expenses == []:
            print('No expenses recorded today')
        else:
            print(f'Day {self.current_day} Expenses: ')
            for item in today_expenses:
                print(item['id'], ' - ' , item['description'], ' - ', item['amount'])
                total += item['amount']
            print('Total spent today: ', total)

    def show_last_expense(self):
        today_expenses = self.all_days[self.current_day]
        if not today_expenses:
            print("No sufficient record")
        else:
            last = today_expenses[-1]
            print("Last expense:")
            print(last['id'], last['description'], last['amount'])

    def end_day(self):
        sum = 0
        one_day = self.all_days[self.current_day]
        for i in one_day:
            sum += i['amount']
        print(f"Day {self.current_day} ended.")
        print("Total spent today:", sum)

        if self.current_day > 1:
            yesterday_total = 0
            yesterday_list = self.all_days[self.current_day - 1]
            for i in yesterday_list:
                yesterday_total += i['amount']
            diff = abs(sum - yesterday_total)
            
            if yesterday_total == sum:
                print('expenses are same as yesterday')
            elif yesterday_total < sum:
                print(f'todays expenses are more than yesterday by {diff}/-')
            else:
                print(f'todays expenses are less than yesterday by {diff}/-')

        else:
            print("No previous record to compare")
        
        if self.current_day < 3:
            self.current_day += 1
        else:
            print("3 days are completed")

tracker = Tracker()
while True:
    print("\n1 -> Add Expense")
    print("2 -> Show Today Expenses")
    print("3 -> Show Last Expense")
    print("4 -> End Day")
    print("5 -> Exit")

    choice = input("enter your choice: ")
    if choice == '1':
        desc = input('Enter description: ')
        amount = int(input("enter amount: "))
        tracker.expense_func(desc,amount)
    elif choice == '2':
        tracker.display_today_expenses()
    elif choice == '3':
        tracker.show_last_expense()
    elif choice == '4':
        tracker.end_day()
    elif choice == '4':
        print('Exit')
        break
    else:
        print('Invalid choice')