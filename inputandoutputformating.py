Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nmae=input()
kavya
>>> name
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> name=input()
kavya
>>> name
'kavya'
>>> name =input("enter your name")
enter your name kavya
>>> name
' kavya'
>>> age=input('enter your age')
enter your age21
>>> age
'21'
>>> age=int(input('enter your age'))
enter your age21
>>> age
21
>>> cgpa=float(input('enter your cgpa'))
enter your cgpa8.9
>>> cgpa
8.9
>>> "praneeth anil sai ram"
'praneeth anil sai ram'
>>>  "praneeth anil sai ram".split()
 
SyntaxError: unexpected indent
>>> "praneeth anil sai ram".split()
['praneeth', 'anil', 'sai', 'ram']
>>> names=input('enter the names').split()
enter the names praneeth anil sai ram
>>> names
['praneeth', 'anil', 'sai', 'ram']
>>> names=input('enter the names').split(,)
SyntaxError: invalid syntax
>>>  names=input('enter the names').split(',')
 
SyntaxError: unexpected indent
>>> names=input('enter the names').split(',')
enter the namespraneeth anil sai ram
>>> names
['praneeth anil sai ram']
>>> names=tuple(input('enter the names').split())
enter the namespraneeth anil sai ram
>>> names
('praneeth', 'anil', 'sai', 'ram')
>>> names=set(input('enter the names').split())
enter the namespraneeth anil sai ram
>>> names
{'ram', 'praneeth', 'sai', 'anil'}
>>> names=input('enter the names').split(',')
enter the namespraneeth anil sai ram
>>> names
['praneeth anil sai ram']
>>> marks=input("enter the marks").split()
enter the marks678 456 789 345 234
>>> marks
['678', '456', '789', '345', '234']
>>> map(int,marks)
<map object at 0x00000226C41D11C0>
>>> list(map(int,marks))
[678, 456, 789, 345, 234]
>>> marks=list(map(int,input("enter the marks").split()))
enter the marks5 8 7 9 2 4 6 7
>>> marks
[5, 8, 7, 9, 2, 4, 6, 7]
>>> marks=tuple(map(int,input("enter the marks").split()))
enter the marks5 8 7 9 2 4 6 7
>>> marks
(5, 8, 7, 9, 2, 4, 6, 7)
>>>  marks=set(map(int,input("enter the marks").split()))
 
SyntaxError: unexpected indent
>>> marks=set(map(int,input("enter the marks").split()))
enter the marks5 8 7 9 2 4 6 7
>>> marks
{2, 4, 5, 6, 7, 8, 9}
>>> gpa=list(map(float,input("enter the gpa").split()))
enter the gpa45 67 89 897
>>> gpa
[45.0, 67.0, 89.0, 897.0]
>>> gpa=tuple(map(float,input("enter the gpa").split()))
enter the gpa45 67 89 897
>>> gpa
(45.0, 67.0, 89.0, 897.0)
>>> gpa=set(map(float,input("enter the gpa").split()))
enter the gpa45 67 89 897
>>> gpa
{89.0, 897.0, 67.0, 45.0}
>>> a=eval(input("enter the value "))
enter the value 98765
>>> type(a)
<class 'int'>
>>> a
98765
>>> a=eval(input("enter the value "))
enter the value 87.456
>>> type(a)
<class 'float'>
>>> a=eval(input("enter the value "))
enter the value "python"
>>> a
'python'
>>> type(a)
<class 'str'>
>>>  a=eval(input("enter the value "))
 
SyntaxError: unexpected indent
>>> a=eval(input("enter the value "))
enter the value [1,2,3,4]
>>> a
[1, 2, 3, 4]
>>> type(a)
<class 'list'>
>>>  a=eval(input("enter the value "))
 
SyntaxError: unexpected indent
>>> a=eval(input("enter the value "))
enter the value (1,2,3,6)
>>> a
(1, 2, 3, 6)
>>> type(a)
<class 'tuple'>
>>> username,password=(1,2)
>>> username
1
>>> password
2
>>> username,password=[1,2]
>>> username
1
>>> username,password=input('enter the usename and password').split()
enter the usename and passwordabc ancd
>>> usename
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    usename
NameError: name 'usename' is not defined
>>> username,password=input('enter the username and password').split()
enter the username and passwordand abgvs
>>> username
'and'
>>> a,b,c=list(map(int,input().split()))
5 6 8
>>> a
5
>>> b
6
>>> c
8
>>> names=input('enter the names').split(',')
enter the nameskavya pandu sreedhar
>>> names
['kavya pandu sreedhar']
>>> names=input('enter the names').split(',')
enter the namespandusreesharkavya
>>> names
['pandusreesharkavya']
>>> a='python'
>>> b=12
>>> c=78,98
>>> d=9.9
>>> print(a,b,c)
python 12 (78, 98)
>>> print('a=','b=','c=',c)
a= b= c= (78, 98)
>>> print('a=',a,'b=',b,'c=',c)
a= python b= 12 c= (78, 98)
>>> print('a=',a,'b=',b,'c=',c,sep='\n')
a=
python
b=
12
c=
(78, 98)
>>> >>> print('a=',a,'b=',b,'c=',c,sep='\t')
SyntaxError: invalid syntax
>>> print('a=',a,'b=',b,'c=',c,sep='\t')
a=	python	b=	12	c=	(78, 98)
>>> print(f'a={a} b={b} c={c}')
a=python b=12 c=(78, 98)
>>> print('a={} b={} c={}'.format(a,b,c))
a=python b=12 c=(78, 98)
>>> print('a=%s b=%d c=%f'%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    print('a=%s b=%d c=%f'%(a,b,c))
TypeError: must be real number, not tuple
>>> print('a=',a,'b=',b,'c=',c,sep='\n',end='@@@')
a=
python
b=
12
c=
(78, 98)@@@
>>> print('a=',a,'b=',b,'c=',c,sep='\n',end='\n\n\n')
a=
python
b=
12
c=
(78, 98)


>>> print('a = %s b = %d c = %f'%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    print('a = %s b = %d c = %f'%(a,b,c))
TypeError: must be real number, not tuple
>>> print('a = %s b = %d d = %f'%(a,b,d))
a = python b = 12 d = 9.900000
>>> print('a={2} b={1} c={0}'.format(a,b,c))
a=(78, 98) b=12 c=python
>>> 