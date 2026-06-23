'''
prices=list(map(int,input("Enter the prices:")))
bill=0
for i in prices:
    bill+=i
print(bill)

pwd=input("enter the string:")
uc=lc=dc=sc=0
for i in pwd:
    if i.isalpha():
        if i.isupper():
            uc+=1
        else:
            lc+=1
    elif i.isdigit():
        dc+=1
    else:
        sc+=1
print("uppercase:",uc)
print("lowercase:",lc)
print("digits:",dc)
print("special characters:",sc)
movies=input("enter the movies:").split()
movies=input("enter the movies:").split()
for i in range(len(movies)):
    print(i+1,'.',movies[i])

records=eval(input())
print("Highest score:",max(records.values()))
print("Lowest score:",min(records.values()))
print("Average salary:",sum(records.values())/len(records))

scores=list(map(int,input("enter the score:").split()))
tr=bd=db=0
for i in scores:
    if i ==4 or i==6:
        bd+=1
    elif i==0:
        db+=1
    tr+=i
print("total runs:",tr)
print("boundaries:",bd)
print("dot balls:",db)

emails=input("enter the email:").split()
for i in emails:
    print(i.split('@')[1])

attempts=0
pin=1234
while attempts<3:
    epin=int(input("enter the pin:"))
    if epin==pin:
        print("Access granted")
        break
    attempts+=1
else:
    print("Card blocked")
c=0
while True:
    items=input("enter the item or exit:")
    if items=="exit":
        print("total items:",c)
        break
    c+=1

at=3
correct='python'
while at>0:
    ans=input("enter the answer:")
    if ans==correct:
        print("You win")
        print("lives remaining",at)
        break
    at-=1
else:
    print("Game over\nlives remaining:0")
s='looping'
i=0
j=len(s)-1
while i<=j:
    print(s[i],s[j])
    i+=1
    j-=1

amount=int(input("enter the amount:"))
notes=[2000,500,100,50,10]
for i in notes:
    req=amount//i
    amount=amount%i
    if req!=0:
        print(req,i)
'''
