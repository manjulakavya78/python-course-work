Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Type "help", "copyright", "credits" or "license()" for more information.
SyntaxError: invalid syntax
>>> l'[]
SyntaxError: EOL while scanning string literal
>>> l=[]
>>> l
[]
>>> l=list()
>>> l
[]
>>> l=[1,2,3,4,56,7,89747,5]
>>> l
[1, 2, 3, 4, 56, 7, 89747, 5]
>>> type(l)
<class 'list'>
>>> id(l)
1694125221568
>>> l.append(12)
>>> l
[1, 2, 3, 4, 56, 7, 89747, 5, 12]
>>> l=[1,2.3,'str',[1,2,3],3+7j,(1,2,3),{1,2,3},{1:2,2:3},false]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    l=[1,2.3,'str',[1,2,3],3+7j,(1,2,3),{1,2,3},{1:2,2:3},false]
NameError: name 'false' is not defined
>>> l=[1,2.3,'str',[1,2,3],3+7j,(1,2,3),{1,2,3},{1:2,2:3},false]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l=[1,2.3,'str',[1,2,3],3+7j,(1,2,3),{1,2,3},{1:2,2:3},false]
NameError: name 'false' is not defined
>>> l=[1,2.3,'str',[1,2,3],3+7j,(1,2,3),{1,2,3},{1:2,2:3}]
>>> l
[1, 2.3, 'str', [1, 2, 3], (3+7j), (1, 2, 3), {1, 2, 3}, {1: 2, 2: 3}]
>>> names=['kavya','sairam','dheera','madhaav','chaitanya']
>>> names
['kavya', 'sairam', 'dheera', 'madhaav', 'chaitanya']
>>> girls=['kavya','sarayu']
>>> girls
['kavya', 'sarayu']
>>> names+girls
['kavya', 'sairam', 'dheera', 'madhaav', 'chaitanya', 'kavya', 'sarayu']
>>> girls*4
['kavya', 'sarayu', 'kavya', 'sarayu', 'kavya', 'sarayu', 'kavya', 'sarayu']
>>> names[1]
'sairam'
>>> names[-1]
'chaitanya'
>>> names[3]
'madhaav'
>>> names[1:2:3]
['sairam']
>>> names[2:3:4]
['dheera']
>>> names[::3]
['kavya', 'madhaav']
>>> names[1::2]
['sairam', 'madhaav']
>>> names[:4:2]
['kavya', 'dheera']
>>> 'kavya'in names
True
>>> 'anil'not in names
True
>>> sorted(names)
['chaitanya', 'dheera', 'kavya', 'madhaav', 'sairam']
>>> sorted(names,reverse=True)
['sairam', 'madhaav', 'kavya', 'dheera', 'chaitanya']
>>> names
['kavya', 'sairam', 'dheera', 'madhaav', 'chaitanya']
>>> max(names)
'sairam'
>>> min(names)
'chaitanya'
>>> len(names)
5
>>> names
['kavya', 'sairam', 'dheera', 'madhaav', 'chaitanya']
>>> names[1]
'sairam'
>>> names[1]='sai kumar'
>>> names
['kavya', 'sai kumar', 'dheera', 'madhaav', 'chaitanya']
>>> 
>>> names[3]='madhavi'
>>> names
['kavya', 'sai kumar', 'dheera', 'madhavi', 'chaitanya']
>>> names.append('sai ram')
>>> names
['kavya', 'sai kumar', 'dheera', 'madhavi', 'chaitanya', 'sai ram']
>>> names.append('ravi')
>>> names
['kavya', 'sai kumar', 'dheera', 'madhavi', 'chaitanya', 'sai ram', 'ravi']
>>> names.insert(1,'madhav')
>>> names
['kavya', 'madhav', 'sai kumar', 'dheera', 'madhavi', 'chaitanya', 'sai ram', 'ravi']
>>> names.extend(['sarayu','anuhya'])
>>> names
['kavya', 'madhav', 'sai kumar', 'dheera', 'madhavi', 'chaitanya', 'sai ram', 'ravi', 'sarayu', 'anuhya']
>>> names.pop()
'anuhya'
>>> names.pop(0)
'kavya'
>>> names
['madhav', 'sai kumar', 'dheera', 'madhavi', 'chaitanya', 'sai ram', 'ravi', 'sarayu']
>>> names.remove('dheera')
>>> names
['madhav', 'sai kumar', 'madhavi', 'chaitanya', 'sai ram', 'ravi', 'sarayu']
>>> del names[1]
>>> names
['madhav', 'madhavi', 'chaitanya', 'sai ram', 'ravi', 'sarayu']
>>> names.clear()
>>> names
[]
>>> names
[]
>>> names.insert[-1,'kav']
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    names.insert[-1,'kav']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> names.remove('ravi')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    names.remove('ravi')
ValueError: list.remove(x): x not in list
>>> names
[]
>>> l=[1,2,3,4,5]
>>> l.pop()
5
>>> 1.pop()
SyntaxError: invalid syntax
>>> l.pop()
4
>>> l.pop()
3
>>> l.pop()
2
>>> l.pop()
1
>>> l
[]
>>> l=[1,2,3]
>>> l
[1, 2, 3]
>>> del[0]
SyntaxError: cannot delete literal
>>> del l[0]
>>> del d
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    del d
NameError: name 'd' is not defined
>>> del l
>>> l
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> l=[1,2,3,4,5,1,2,33,2,5,6]
>>> l.index(3)
2
>>> l.count()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    l.count()
TypeError: count() takes exactly one argument (0 given)
>>> l.count(1)
2
>>> l=[1,2,3]
>>> n=1
>>> n
1
>>> n=l
>>> n
[1, 2, 3]
>>> l
[1, 2, 3]
>>> n.append(3)
>>> n
[1, 2, 3, 3]
>>> n=l.copy()
>>> n.append(10)
>>> n
[1, 2, 3, 3, 10]
>>> l
[1, 2, 3, 3]
>>> sum(n)
19
>>> any([1,23,4])
True
>>> any([0,0,0])
False
>>> all([1,22,3,0])
False
>>> all([1,34,4])
True
>>> 