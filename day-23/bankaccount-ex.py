class BankAccount:
    def __init__(self,person):
        self.person=person
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient balance")
    def show_balance(self):
        print(f"Balance:{self.balance}")
a=BankAccount("kavya")
a.deposit(100)
a.withdraw(50)
a.show_balance()
