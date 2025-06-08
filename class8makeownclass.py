class bank_account:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        
    def withdraw (self, withdraw):
        if withdraw < self.balance:
            self.balance = self.balance - withdraw
        else:
            print("you have insufficient funds")

    def get_balance (self):
        return(self.balance)
    

myacct = bank_account("Alice", 500)
myacct.deposit(500)
myacct.withdraw(1000)
print (myacct.get_balance())
        