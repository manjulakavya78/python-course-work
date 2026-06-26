Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> c=10
>>> type(c)
<class 'int'>
>>> s=s+'lang'
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s=s+'lang'
NameError: name 's' is not defined
>>> s='python'
>>> s=s+'lang'
>>> s
'pythonlang'
>>> id(s)
1279747419568
>>> s=s+'programming'
>>> s
'pythonlangprogramming'
>>> id(s)
1279786703088
>>> l=[1,2,3,5]
>>> id(l)
1279787562816
>>> l.append(34)
>>> l
[1, 2, 3, 5, 34]
>>> id(l)
1279787562816
>>> s={1,2,3,45,45,67}
>>> s
{1, 2, 67, 3, 45}
>>> type(s)
<class 'set'>
>>> s=set()
>>> s
set()
>>> type(s)
<class 'set'>
>>> s={}
>>> type(s)
<class 'dict'>
>>> d={'name:'kavya','batchno':56,'course':'pfs'}
   
SyntaxError: invalid syntax
>>> d={'name':'kavya','batchno':56,'course':'pfs'}
>>> d
{'name': 'kavya', 'batchno': 56, 'course': 'pfs'}
>>> a=none
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a=none
NameError: name 'none' is not defined
>>> d=none
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d=none
NameError: name 'none' is not defined
>>> h=none
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    h=none
NameError: name 'none' is not defined
>>> t=(1,2,3,4,4,5,6,6,6)
>>> t
(1, 2, 3, 4, 4, 5, 6, 6, 6)
>>> type(t)
<class 'tuple'>
>>> t=()
>>> t
()
>>> 