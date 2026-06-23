'''
int
while condition:
    statments
    upd
bill
guess the number
chatbot
i=1
while i<=10:
    print(i)
    i+=1

i=30
while i<=50:
    print(i)
    i+=2

i=6
while i<100:
    print(i)
    i+=6


i=10
while i>=1:
    print(i)
    i-=1

i=29
while i>=1:
    print(i)
    i-=2

s='python'
i=0
while i<len(s):
    print(i,s[i])
    i+=1

s=[1,2,3,4,5,5,6,7,7,8]
i=0
while i <len(s):
    print(i,s[i])
    i+=1

i=0
while i<=10:
    i+=1
    if i==5:
        continue
    print(i)
i=10
while i<=10:
    pass
x=10
y=10
z=None
assert x!=None and y!=None and z!=None,"you need to update"
print(x,y,z)
api=''
assert api!='','update api'

l=[]
while True:
    product=input("enter the product:")
    price=float(input("enter the price:"))
    quantity=int(input("enter the quantity:"))
    l.append([product,price,quantity])
    status=input('[d]one or [n]ext:').upper()
    if status == "D":
        bill=0
        for i in l:
            print(f'{i[0]}:{i[1]} *{i[2]}={i[1]*i[2]}')
            bill+=i[1]*i[2]
        print(f"total bill: ${bill}")
        print("thanks for shopping")
        break

number=5
while True:
    n=int(input("guess the number:"))
    if number==n:
        print("your gues is correct")
        break
    else:
        print("incorrect")
'''
l=[9,0,0,2,3,4,5,6]
while 0 in l:
    l.remove(0)
print(l)
