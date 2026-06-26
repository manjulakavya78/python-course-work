'''def isprime(num):
    for i in range(2,num):
        if num%i==0:
           return f"{num}-Not a prime number"
   
    return f"{num}-prime number"
print(isprime(12))'''


def isprime(n):
    for num in range(2,n+1):
        for i in range(2,num):
           if num%i==0:
               break
        else:
            print(num,end='\n')
           
   
   
isprime(50)
