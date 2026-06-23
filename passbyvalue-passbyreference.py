'''def update(n):
    n=True
    print("Inside:",n)
n=False
update(n)
print("Outside:",n)

def update(n):
    n+=10
    print("Inside:",n)
n=10
update(n)
print("Outside:",n)

def update(n):
    n+=10
    print("Inside:",n)
n=10.9
update(n)
print("Outside:",n)


def update(n):
    n+=10
    print("Inside:",n)
n=10.9+5j
update(n)
print("Outside:",n)'''
'''
def update(n):
    n=n.upper()
    print("Inside:",n)
n="python"
update(n)
print("Outside:",n)
'''
'''
def update(n):
    n.append(40)
    print("Inside:",n)
n=[10,20,30]
update(n)
print("Outside:",n)

'''
'''
def update(n):
    n.insert(40,50)
    print("Inside:",n)
n=(10,20,30)
update(n)
print("Outside:",n)
'''
def update(n):
    n=n.update({'3:30','4:40'})
    print("Inside:",n)
n={'1:10','2:20'}
update(n)
print("Outside:",n)

