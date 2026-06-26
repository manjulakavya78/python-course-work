'''
import logic()
logic.login()
logic.main()
'''
'''
import login as lg
lg.login()
lg.menu()
'''
'''
from logic import menu,data
menu()
print(data)
'''
'''
from logic import *
menu()
login()
print(data)
'''

import logic as lg

if lg.login():
    print("========Welcome to ATM===========")
    while True:
        lg.menu()
        ch = input("Enter your choice: ").upper()
        if ch == 'C':
            lg.checkBalance()
        elif ch == 'D':
            lg.deposit()
        elif ch == 'W':
            lg.withdraw()
        elif ch == 'V':
            lg.viewTransactions()
        elif ch == 'E':
            print("==========Thankyou===========")
            break
        
    
    
    
