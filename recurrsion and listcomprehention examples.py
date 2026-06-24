'''
def sumofn(n):
    if n==0:
        return 0
    return n+sumofn(n-1)
    
n=int(input('Enter the n:'))
print(sumofn(n))
    

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
    
n=int(input('Enter the n:'))
print((factorial(n)))
    

def sumofdigits(n):
    if n==0:
        return 0
    return n*10+sumofdigits(n//10)
n=int(input("Enter the n:"))
print(sumofdigits(n))
    

    
def power(base,pow):
    if pow==0:
        return 1
    return base * power(base,pow-1)
print(power(2,5))
print(power(3,4))
print(power(5,3))

def display(s,ind):
    if len(s)+1 == ind:
        return
    print(s[:ind])
    display(s,ind+1)
display('python programming',1)

def display(s,ind,wid):
    if ind == len(s)-wid+1:
        return
    print(s[ind:ind+wid])
    display(s,ind+1,wid)
display('python programming',0,15)


l=[1,2,3,4,5,6]
res1=[]
for i in l:
    res1.append(i*i)
res2=[i*i for i in l]
print(res1,res2)

s='PYTHON PROGRAMMING'
res=[i for i in s if i in 'aeiusAEIOUS']
print(res)





s=[2,4,7,12,53,56,34,23,67,23,90,79,35]
res=[i if i%2==0 else 0 for i in s]
print(res)


res=[j for i in range(5) for j in range(1,4)]
print(res)



res=[[j for j in range(1,4)]for i in range(5)]
print(res)
'''
res={i:i**2 for i in range(1,11)}
print(res)
     
