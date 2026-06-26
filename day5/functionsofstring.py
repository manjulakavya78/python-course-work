Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='python programming'
>>> s
'python programming'
>>> s.startswith('py')
True
>>> s.endswith('ing')
True
>>> "abc".isalpha()
True
>>> 'hbduedbbmdmanje'.isalpha()
True
>>> '977654577'.isalnum()
True
>>> 'hsn'.isupper()
False
>>> 'AHHB'.isupper()
True
>>> 'jje'.islower()
True
>>> 'helo worls'.isspace()
False
>>> ' '.isspace()
True
>>> 'Abh Sghj'.istitle()
True
>>> 'AASS jrhdnhn'.istitle()
False
>>> 'my_val'.isidentifier()
True
>>> '1232'.isdigit()
True
>>> '27129180.22221'.isdecimal()
False
>>> '2928.21212'.isdecimal()
False
>>> l=[]
>>> l
[]
>>> l=list[]
SyntaxError: invalid syntax
>>> l=list()
>>> l
[]
>>> l=[1,2,3,4,5]
>>> l
[1, 2, 3, 4, 5]
>>> type(l)
<class 'list'>
>>> id(l)
1571738903296
>>> 1.append(12)
SyntaxError: invalid syntax
>>> l.append(12)
>>> l
[1, 2, 3, 4, 5, 12]
>>> l
