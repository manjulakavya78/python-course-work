'''
def primenumber(num):
    res=[]
    for n in range(2,num+1):
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            res.append(n)
    return res
            
def generators(res):
    for i in res:
        yield i
res=primenumber(50)
gen=generators(res)

for i in range(len(res)):
    print(next(gen))
    

'''
'''
def primenumber(num):
    res=[]
    for n in range(2,num+1):
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            res.append(n)
    return res
            
res=primenumber(50)
print(res)
'''
