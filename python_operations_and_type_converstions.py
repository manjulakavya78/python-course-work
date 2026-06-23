Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=20
>>> b=10
>>> a+b
30
>>> a-b
10
>>> a*b
200
>>> a%b
0
>>> a/b
2.0
>>> a//b
2
>>> 4**2
16
>>> 8**2
64
>>> a**2
400
>>> 10/3
3.3333333333333335
>>> a
20
>>> b
10
>>> a<b
False
>>> a>b
True
>>> a>=b
True
>>> a<=b
False
>>> a==b
False
>>> a!=b
True
>>> a
20
>>> a=a+10
>>> a=a+10
>>> a
40
>>> a+=10
>>> a
50
>>> a-=10
>>> a
40
>>> a//=2
>>> a
20
>>> a**=2
>>> a
400
>>> a%=3
>>> a
1
>>> a/=1
>>> a
1.0
>>> s='ptyhon'
>>> s[0]=='p'
True
>>> s[-1]=='n'
True
>>> s[0]=='p' and s[-1]=='n'
True
>>> s='python programming'
>>> s[0]=='p' or s[-1]=='n'
True
>>>  not s[-1]=='n'
 
SyntaxError: unexpected indent
>>> not  s[-1]=='n'
True
>>> #str list tuple set dict
>>> 'python' in s
True
>>> 'py' in s
True
>>> 'java' in s
False
>>> 'g' in s
True
>>> 'z' not in s
True
>>> 'th' not in s
False
>>> l
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> l=['laptop','mouse','shints','shoes']
>>> 'mouse' in l
True
>>> 'tr' in l
False
>>> 'tv' not in l
True
>>> t=(1,2,3,4,5,6,7,8,9)
>>> 2 in t
True
>>> 9 in t
True
>>> 0 in t
False
>>> 17 not in t
True
>>> s={6,"seven",8,"nine",10,"eleven"}
>>> 6 in s
True
>>> 9 in s
False
>>> 7 not in s
True
>>> seven not in s
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    seven not in s
NameError: name 'seven' is not defined
>>> "seven" not in s
False
>>> d={'name':'sairam','batch':56,'email':'s@gmail.com'}
>>> 'name' in d
True
>>> 'sairam' in d
False
>>> l=[1,2,3,4]
>>> m=[1,2,3,4]
>>> l is m
False
>>> n=m
>>> n
[1, 2, 3, 4]
>>> n == n
True
>>> n is m
True
>>> id(l)
2888809907904
>>> id(m)
2888809823616
>>> id(n)
2888809823616
>>> l is m
False
>>> l is not m
True
>>> n is m
True
>>> m is  not n
False
>>> m is n
True
>>> 11$12
SyntaxError: invalid syntax
>>> 11&12
8
>>> 11/12
0.9166666666666666
>>> 11|12
15
>>> 11^12
7
>>> 11!12
SyntaxError: invalid syntax
>>> ~12
-13
>>> 2<<2
8
>>> 3>>2
0
>>> 10>>2
2
>>> float(a)
1.0
>>> a=10
>>> a
10
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> bool(a)
True
>>> b=10.3
>>> int(b)
10
>>> str(b)
'10.3'
>>> complex(b)
(10.3+0j)
>>> bool(b)
True
>>> c=3+3j
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    int(c)
TypeError: can't convert complex to int
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    float(c)
TypeError: can't convert complex to float
>>> str(c)
'(3+3j)'
>>> list(c)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
>>> bool(c)
True
>>> a='pytho'
>>> b='10'
>>> c='10.3'
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'pytho'
>>> int(b)
10
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    int(c)
ValueError: invalid literal for int() with base 10: '10.3'
>>> float(a)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    float(a)
ValueError: could not convert string to float: 'pytho'
>>> float(b)
10.0
>>> float(c)
10.3
>>> complex(b)
(10+0j)
>>> complex(c)
(10.3+0j)
>>> list(a)
['p', 'y', 't', 'h', 'o']
>>> list(b)
['1', '0']
>>> list(c)
['1', '0', '.', '3']
>>> tuple(a)
('p', 'y', 't', 'h', 'o')
>>> tuple(b)
('1', '0')
>>> tuple(c)
('1', '0', '.', '3')
>>> set(a)
{'y', 't', 'p', 'h', 'o'}
>>> set(b)
{'1', '0'}
>>> set(c)
{'1', '0', '.', '3'}
>>> bool(a)
True
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ll=[1,2,3,4,5]
>>> l
[1, 2, 3, 4]
>>> str(l)
'[1, 2, 3, 4]'
>>> bool(l)
True
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> tuple(l)
(1, 2, 3, 4)
>>> set(l)
{1, 2, 3, 4}
>>> t=(1,2,3,4,5)
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> bool(t)
True
>>> list(t)
[1, 2, 3, 4, 5]
>>> set(t)
{1, 2, 3, 4, 5}
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> s={1,2,3,4,5,6,7}
>>> bool(s)
True
>>> str(s)
'{1, 2, 3, 4, 5, 6, 7}'
>>> list(s)
[1, 2, 3, 4, 5, 6, 7]
>>> tuple(S)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    tuple(S)
NameError: name 'S' is not defined
>>> tuple(s)
(1, 2, 3, 4, 5, 6, 7)
>>> d={1:2,2:4,3:6}
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
>>> str(d)
'{1: 2, 2: 4, 3: 6}'
>>> list(d)
[1, 2, 3]
>>> vool(d)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    vool(d)
NameError: name 'vool' is not defined
>>> bool(d)
True
>>> set(d)
{1, 2, 3}
>>> tuple(d)
(1, 2, 3)
>>> s=true
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    s=true
NameError: name 'true' is not defined
>>> s=true
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    s=true
NameError: name 'true' is not defined
>>> s=true
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    s=true
NameError: name 'true' is not defined
>>> g=true
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    g=true
NameError: name 'true' is not defined
>>> 