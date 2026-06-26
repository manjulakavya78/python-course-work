'''def display(name,email):
    print('name:',name)
    print('email',email)

display('madhav','madhav@gmail.com')
display('bharath@gmail.com','bharath')


def display(name,email):
    print('name:',name)
    print('email',email)

display(name='madhav',email='madhav@gmail.com')
display(email='bharath@gmail.com',name='bharath')


def display(name,email='',password=''):
    print('name:',name)
    print('email',email)
    print('password',password)
display('madhav')
display('madhav','madhav@gmail.com','madhav@123')
display('bharath@gmail.com','bharath')


def display(*num):
    print('nums:',num)
display(1)
display(1,2,3,4,5)
display(1,4,6,7)
display(1,4)
'''
def display(**num):
    print('nums:',num)
display(k1=1)
display(k1=1,k2=2,k3=3,)
display(k1=1,k2=2)
