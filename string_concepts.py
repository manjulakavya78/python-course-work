Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=''
>>> s=""
>>> s"python programming"
SyntaxError: invalid syntax
>>> s='python programming'
>>> s
'python programming'
>>> 'python'+'lang'
'pythonlang'
>>> fname='kavya'
>>> sname='manjula'
>>> fname+sname
'kavyamanjula'
>>> s='python'
>>> s*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
>>> 'python lang'
'python lang'
>>> s(10)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s(10)
TypeError: 'str' object is not callable
>>> s='python'
>>> s(3)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s(3)
TypeError: 'str' object is not callable
>>> s[3]
'h'
>>> s='kavya kavitha anil'
>>> s[0]
'k'
>>> s[3]
'y'
>>> s[10]
't'
>>> s[-1]
'l'
>>> s[:5]
'kavya'
>>> s[6:14]
'kavitha '
>>> s[::-1]
'lina ahtivak ayvak'
>>> s[-5:]
' anil'
>>> s[-1:-6:-1]
'lina '
>>> s[-6:-19:-1]
'ahtivak ayvak'
>>> s[::2]
'kvakvtaai'
>>> s[1::2]
'ay aih nl'
>>> 'kavya'in s
True
>>> s
'kavya kavitha anil'
>>> len(s)
18
>>> ord('k')
107
>>> s
'kavya kavitha anil'
>>> sorted('s')
['s']
>>> sorted(s)
[' ', ' ', 'a', 'a', 'a', 'a', 'a', 'h', 'i', 'i', 'k', 'k', 'l', 'n', 't', 'v', 'v', 'y']
>>> max(s)
'y'
>>> min(s)
' '
>>> ord(' ')
32
>>> s
'kavya kavitha anil'
>>> s="Kavya Anil Rahul"
>>> s
'Kavya Anil Rahul'
>>> s.upper()
'KAVYA ANIL RAHUL'
>>> s.lower()
'kavya anil rahul'
>>> s.swapcase()
'kAVYA aNIL rAHUL'
>>> s.captilize()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.captilize()
AttributeError: 'str' object has no attribute 'captilize'
>>> s.capitalize()
'Kavya anil rahul'
>>> s.title()
'Kavya Anil Rahul'
>>> s.center(60,'*')
'**********************Kavya Anil Rahul**********************'
>>> s.center(60,'--')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s.center(60,'--')
TypeError: The fill character must be exactly one character long
>>> s.center(60,'-')
'----------------------Kavya Anil Rahul----------------------'
>>> s.center(45,'@')
'@@@@@@@@@@@@@@@Kavya Anil Rahul@@@@@@@@@@@@@@'
>>> s.rjust(45,'#')
'#############################Kavya Anil Rahul'
>>> s.ljust(45,'*')
'Kavya Anil Rahul*****************************'
>>> '45'.zfill(4)
'0045'
>>> '78'.zfill(80)
'00000000000000000000000000000000000000000000000000000000000000000000000000000078'
>>> '89'zfill(9)
SyntaxError: invalid syntax
>>> '89'.zfill(9)
'000000089'
>>> s.find('A')
6
>>> s.find('z')
-1
>>> s.rfind('t')
-1
>>> s.lfind('t')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s.lfind('t')
AttributeError: 'str' object has no attribute 'lfind'
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.count('a')
3
>>> s.count('i')
1
>>> s.split()
['Kavya', 'Anil', 'Rahul']
>>> s='''multi
line
comment'''
>>> s
'multi\nline\ncomment'
>>> s.splitlines()
['multi', 'line', 'comment']
>>> s='Kavya Anil Rahul'
>>> s.partition(' ')
('Kavya', ' ', 'Anil Rahul')
>>> s.partition('A')
('Kavya ', 'A', 'nil Rahul')
>>> s.partition('v')
('Ka', 'v', 'ya Anil Rahul')
>>> s.rpartition('v')
('Ka', 'v', 'ya Anil Rahul')
>>> ' '.join(s)
'K a v y a   A n i l   R a h u l'
>>> ''.join(s)
'Kavya Anil Rahul'
>>> s='      hello      worls    '
>>> s
'      hello      worls    '
>>> s.strip()
'hello      worls'
>>> s.lstrip()
'hello      worls    '
>>> s.rstrip()
'      hello      worls'
>>> s='python programming'
>>> s
'python programming'
>>> s.replace('python','java')
'java programming'
>>> s
'python programming'
>>> s.maketrans('aeiou','*****')
{97: 42, 101: 42, 105: 42, 111: 42, 117: 42}
>>> s.translate(s.maketrans('aeiou','*****'))
'pyth*n pr*gr*mm*ng'
>>> s='Hell0 😉'
>>> s
'Hell0 😉'
>>> s.encode()
b'Hell0 \xf0\x9f\x98\x89'
>>> s.decode
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    s.decode
AttributeError: 'str' object has no attribute 'decode'
>>> s.decode()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s.decode()
AttributeError: 'str' object has no attribute 'decode'
>>> b'Hell0 \xf0\x9f\x98\x89'.decode
<built-in method decode of bytes object at 0x00000226E3600FC0>
>>> b'Hell0 \xf0\x9f\x98\x89'.decode()
'Hell0 😉'
>>> 
