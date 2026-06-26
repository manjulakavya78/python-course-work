data = {
    123456:{'pin':1234,'balance':8000,'history':[]},
    234561:{'pin':1111,'balance':5000,'history':[]},
    345612:{'pin':1222,'balance':6000,'history':[]},
    456123:{'pin':1233,'balance':7000,'history':[]},
    }

def login():
    global acc_num
    acc_num = int(input("Enter the account number: "))
    pin = int(input("Enter the pin: "))
    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login Successful")
        return True
    else:
        print("Invalid details")
        return False

def menu():
    print('[C]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Trasactions')
    print('[E]xit')


def checkBalance():
    print(f"Current Balance: {data[acc_num]['balance']}")


def deposit():
    amount = int(input("Enter the amount: "))
    data[acc_num]['balance']+=amount
    data[acc_num]['history'].append(f'{amount} deposit +++++++++')
    print("Deposit Successfully\n")

def withdraw():
    amount = int(input("Enter the amount: "))
    if amount <= data[acc_num]['balance']:
        data[acc_num]['balance']-=amount
        data[acc_num]['history'].append(f'{amount} withdraw --------')
        print("Withdraw Successfully\n")
    else:
        print("Insuffienct balance")

def viewTransactions():
    if data[acc_num]['history']:
        print("---------Transactions-------")
        for i in data[acc_num]['history']:
            print(i)
        print("End of Transactions")
    else:
        print("No Trasactions")
