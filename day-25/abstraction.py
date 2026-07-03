from abc import ABC,abstractmethod

class bankaccount:
    def checkbalance(self):
        print("you can check your balance")
    def viewhistory(self):
        print("you can check the transactions")
    @abstractmethod
    def deposit_withdraw(self):
        pass
class savingsaccount(bankaccount):
    def deposit__withdraw(self):
        print("Deposit withdraw-savings account")
        
class jointaccount(bankaccount):
    def deposit__withdraw(self):
        print("Deposit withdraw-joint account")    
class currentaccount(bankaccount):
    def deposit__withdraw(self):
        print("Deposit withdraw-current account")
class salaryaccount(bankaccount):
    def deposit__withdraw(self):
        print("Deposit withdraw-salary account")

manoj=savingsaccount()
manoj.deposit_withdraw()
manoj.viewhistory()
manoj.checkbalance()

krishna=jointaccount()
krishna.deposit_withdraw()
krishna.viewhistory()
krishna.checkbalance()

venky=currentaccount()
venky.deposit_withdraw()
venky.viewhistory()
venky.checkbalance()

sree=salaryaccount()
sree.deposit_withdraw()
sree.viewhistory()
sree.checkbalance()
