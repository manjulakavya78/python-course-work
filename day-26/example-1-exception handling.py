try:
    balance=5000
    amount = int(input())
    if amount < 0:
        raise Exception("Amount needs to be > 0")

except Exception as e:
    print("Error occured:",e)
else:
    balance-=amount
    print("Withdraw Successful",balance)
finally:
    print("End the block")
