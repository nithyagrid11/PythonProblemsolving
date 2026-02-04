class Bank:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        print(f"Account Owner: {self.owner} and Account Balance: {self.balance}")

    def deposit(self,deposit_amount):
        self.balance += deposit_amount
        print(f"Amount: {deposit_amount} is depositied")
        print('Deposit done')
        print(f"Account Owner: {self.owner} and Current Balance: {self.balance}")

    def withdraw(self,withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print(f"Amount: {withdraw_amount} is withdrawn ")
            print('Withdrawn done')
            print(f'Current new balance is {self.balance}')
        else:
            print('Balance is low')
b1 = Bank('Nithya',500)
b1.deposit(100)
b1.withdraw(200)
#practised the challenge gave in udemy