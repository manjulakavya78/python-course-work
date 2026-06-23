Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=(1)
>>> t
1
>>> t=(1,)
>>> t
(1,)
>>> t=(1,2,3,4,5)
>>> t=()
>>> t=tuple()
>>> type()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
>>> type(t)
<class 'tuple'>
>>> t=(1,2,3,4,5)
>>> t
(1, 2, 3, 4, 5)
>>> t=t(1)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t=t(1)
TypeError: 'tuple' object is not callable
>>> t=(1)
>>> t
1
>>> t=(1,)
>>> t
(1,)
>>> t=(1,2,3,4,5)
>>> t
(1, 2, 3, 4, 5)
>>> t=(1,1,1)
>>> t
(1, 1, 1)
>>> (1,2,3)+(3,4,5)
(1, 2, 3, 3, 4, 5)
>>> (1,2,3)*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> t
(1, 1, 1)
>>> t=(1,2,3,4,6,8,9,2,1,4,6)
>>> T[2]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    T[2]
NameError: name 'T' is not defined
>>> t[2]
3
>>> t[3]
4
>>> t[0]
1
>>> t[-2]
4
>>> t
(1, 2, 3, 4, 6, 8, 9, 2, 1, 4, 6)
>>> t[6:9]
(9, 2, 1)
>>> t[::-1]
(6, 4, 1, 2, 9, 8, 6, 4, 3, 2, 1)
>>> t[-1:-5:-1]
(6, 4, 1, 2)
>>> t
(1, 2, 3, 4, 6, 8, 9, 2, 1, 4, 6)
>>> 8 in t
True
>>> 9 in t
True
>>> 11 in t
False
>>> 2 not in t
False
>>> t
(1, 2, 3, 4, 6, 8, 9, 2, 1, 4, 6)
>>> t.index(3)
2
>>> t.count(6)
2
>>> sorted(t)
[1, 1, 2, 2, 3, 4, 4, 6, 6, 8, 9]
>>> max(t)
9
>>> min(t)
1
>>> len(t)
11
>>> any((1,2,3,4))
True
>>> any((1,0))
True
>>> all((1,2,3,4))
True
>>> all((1,0))
False
>>> a,b,c=(1,2,3)
>>> a
1
>>> b
2
>>> c
3
>>> a=(1,2,3,4)
>>> a
(1, 2, 3, 4)
>>> w,x,y,z=a
>>> w
1
>>> x
2
>>> y
3
>>> zz
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    zz
NameError: name 'zz' is not defined
>>> t=(1,12.3,"string",[1,2,3],(1,2,3),{1,2,3},{1:2,2:2,3:3},False,None)
>>> t
(1, 12.3, 'string', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 2, 2: 2, 3: 3}, False, None)
>>> t[0]
1
>>> t[0]=12
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    t[0]=12
TypeError: 'tuple' object does not support item assignment
>>> 