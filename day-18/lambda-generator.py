'''
wish=lambda name:f'Welcome to the course,{name}'
   
print(wish('kavya'))
print(wish('sruthi'))



greater=lambda a,b:a if a>b else b
print(greater(10,8))
print(greater(19,12))
print(greater(1,8))


avg=lambda a,b,c:(a+b+c)/3
print(avg(10,8,6))
print(avg(19,12,5))
print(avg(1,8,6))

gst=lambda p:p+p*0.18
print(gst(1000))
print(gst(10000))
print(gst(999999))



l=[1,2,3,4,5]
res1=list(map(lambda i:i*i,l))
print(res1)




s=[12,23,34,45,56,67]
res2=list(filter(lambda i:i%3==0,s))
print(res2)

from functools import reduce

k=[10,20,30,40]
res3 = reduce(lambda sum,i:sum+i,k)
print(res3)


..l={'laptop':50000,'phone':100000,'charger':1000,'mouse':800}
res1=dict(map(lambda i:(i[0],i[1]+i[1]*0.18),l.items()))
print(res1)



l={'laptop':0,'phone':10,'charger':2,'mouse':0}
res1=list(filter(lambda i:l[i]!=0,l))
print(res1)

l={'laptop':50000,'phone':100000,'charger':1000,'mouse':800}
res1=dict(map(lambda i:(i[0],i[1]+i[1]*0.18),l.items()))
print(res1)
h21= dict(sorted(l.items(),key=lambda i:i[1],reverse=True))
print(h21)
l2h=dict(sorted(l.items(),key=lambda i:i[1]))
print(l2h)

def reels():
    l=['1..50','51..100','101...150','151..200','201..250','251..300']
    for i in range(len(l)):
        yield l[i]
r=reels()
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))

def reels():
    l=['1..50','51..100','101...150','151..200','201..250','251..300']
    for i in range(len(l)):
        yield l[i]
r=reels()
while True:
    try:
        print(next(r))
    except StopIteration:
        print("End if the reels")
        break



def factors(n):
    return [i for i in range(1,n+1) if n%i==0]
def generators(res):
    for i in res:
        yield i
        
res=factors(30)
f=generators(res)
for i in range(len(res)):
    print(next(f))


def primenumbers(n):
    return [num for num in range(2, n+1) if sum(1 for i in range(1, num+1) if num % i == 0) == 2]

def generators(res):
    for i in res:
        yield i
        
res = primenumbers(30)
f = generators(res)

for i in range(len(res)):
    print(next(f))
'''

def fib(n):
    if n==1:
        return [0]
    elif n==2:
        return[0,1]
    elif n>2:
        res=[0,1]
        a,b=0,1
        for i in range(n-2):
            c=a+b
            res.append(c)
            a,b=b,c
        return res
def generators(res):
    for i in res:
        yield i
res=fib(13)
f=generators(res)

for i in range(len(res)):
    print(next(f))
        
    

