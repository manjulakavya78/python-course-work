pin=1234
for i in range(5):
    epin=int(input("Enter the pin:"))
    if pin==epin:
       print("Unlock the phone")
       break
    else :
       print("Incorrect pin,try again")
else:
    print("Try after 60 seconds")
