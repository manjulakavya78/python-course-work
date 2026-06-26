Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={}
>>> d=dict()
>>> type(d)
<class 'dict'>
>>> d={1:2,2:4,3:9,4:16,5:25}
>>> d
{1: 2, 2: 4, 3: 9, 4: 16, 5: 25}
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d[0]
KeyError: 0
>>> 25 in d
False
>>> 3 in d
True
>>> 5 in d
True
>>> 40 not ind
SyntaxError: invalid syntax
>>> 40 not in d
True
>>> d={}
>>> d[1]='int'
>>> d[12.4]='flo'
>>> d
{1: 'int', 12.4: 'flo'}
>>> d["string']='str'
  
SyntaxError: EOL while scanning string literal
>>> d("string")='str'
SyntaxError: cannot assign to function call
>>> d["string"]='str'
>>> d[[1,2,3]]="list"
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d[[1,2,3]]="list"
TypeError: unhashable type: 'list'
>>> d[[1,2,3]]='list'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: unhashable type: 'list'
>>> d[2+3j]='com'
>>> d[False]='bool'
>>> d
{1: 'int', 12.4: 'flo', 'string': 'str', (2+3j): 'com', False: 'bool'}
>>> d[1]='integer'
>>> d
{1: 'integer', 12.4: 'flo', 'string': 'str', (2+3j): 'com', False: 'bool'}
>>> d={}
>>> d[1]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d[1]
KeyError: 1
>>> d[2]=12.3
>>> d[3]='str'
>>> d[4]=[1,2,3]
>>> d[5]=(1,2,3)
>>> d[6]={1,23}
>>> d[7]={1:1,2:2}
>>> d[8]=2+4j
>>> d[9]=True
>>> d[10]=None
>>> d
{2: 12.3, 3: 'str', 4: [1, 2, 3], 5: (1, 2, 3), 6: {1, 23}, 7: {1: 1, 2: 2}, 8: (2+4j), 9: True, 10: None}
>>> d[11]=1
>>> d[12]=1
>>> d[13]=1
>>> d
{2: 12.3, 3: 'str', 4: [1, 2, 3], 5: (1, 2, 3), 6: {1, 23}, 7: {1: 1, 2: 2}, 8: (2+4j), 9: True, 10: None, 11: 1, 12: 1, 13: 1}
>>> d[1]=1
>>> d
{2: 12.3, 3: 'str', 4: [1, 2, 3], 5: (1, 2, 3), 6: {1, 23}, 7: {1: 1, 2: 2}, 8: (2+4j), 9: True, 10: None, 11: 1, 12: 1, 13: 1, 1: 1}
>>> d[4]=[1,2,3]
>>> 
>>> d[4]
[1, 2, 3]
>>> d[5]
(1, 2, 3)
>>> d[9]
True
>>> d[30]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    d[30]
KeyError: 30
>>> d.get(30)
>>> d
{2: 12.3, 3: 'str', 4: [1, 2, 3], 5: (1, 2, 3), 6: {1, 23}, 7: {1: 1, 2: 2}, 8: (2+4j), 9: True, 10: None, 11: 1, 12: 1, 13: 1, 1: 1}
>>> d.get(30)
>>> d[12]
1
>>> d.get(30,"key is not present")
'key is not present'
>>> d.get(12,'key is not present')
1
>>> d
{2: 12.3, 3: 'str', 4: [1, 2, 3], 5: (1, 2, 3), 6: {1, 23}, 7: {1: 1, 2: 2}, 8: (2+4j), 9: True, 10: None, 11: 1, 12: 1, 13: 1, 1: 1}
>>> id(d)
1416538096704
>>> d[4]=20
>>> d
{2: 12.3, 3: 'str', 4: 20, 5: (1, 2, 3), 6: {1, 23}, 7: {1: 1, 2: 2}, 8: (2+4j), 9: True, 10: None, 11: 1, 12: 1, 13: 1, 1: 1}
>>> id(d)
1416538096704
>>> d[8]=40
>>> d
{2: 12.3, 3: 'str', 4: 20, 5: (1, 2, 3), 6: {1, 23}, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 11: 1, 12: 1, 13: 1, 1: 1}
>>> d[5]=30
>>> d
{2: 12.3, 3: 'str', 4: 20, 5: 30, 6: {1, 23}, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 11: 1, 12: 1, 13: 1, 1: 1}
>>> d[15]=101
>>> d
{2: 12.3, 3: 'str', 4: 20, 5: 30, 6: {1, 23}, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 11: 1, 12: 1, 13: 1, 1: 1, 15: 101}
>>> d.update({16:17,17:111111111111})
>>> d
{2: 12.3, 3: 'str', 4: 20, 5: 30, 6: {1, 23}, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 11: 1, 12: 1, 13: 1, 1: 1, 15: 101, 16: 17, 17: 111111111111}
>>> d.popitem()
(17, 111111111111)
>>> d.popitem()
(16, 17)
>>> d.popitem(6)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d.popitem(6)
TypeError: popitem() takes no arguments (1 given)
>>> d.pop(6)
{1, 23}
>>> del d[3]
>>> d
{2: 12.3, 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 11: 1, 12: 1, 13: 1, 1: 1, 15: 101}
>>> d.clear()
>>> d
{}
>>> d={2: 12.3, 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 11: 1, 12: 1, 13: 1, 1: 1, 15: 101}
>>> d.keys()
dict_keys([2, 4, 5, 7, 8, 9, 10, 11, 12, 13, 1, 15])
>>> d.values()
dict_values([12.3, 20, 30, {1: 1, 2: 2}, 40, True, None, 1, 1, 1, 1, 101])
>>> d.items()
dict_items([(2, 12.3), (4, 20), (5, 30), (7, {1: 1, 2: 2}), (8, 40), (9, True), (10, None), (11, 1), (12, 1), (13, 1), (1, 1), (15, 101)])
>>> sorted(d)
[1, 2, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15]
>>> min(d)
1
>>> max(d)
15
>>> len(d)
12
>>> d
{2: 12.3, 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 11: 1, 12: 1, 13: 1, 1: 1, 15: 101}
>>> n=d
>>> n[10]=134
>>> n
{2: 12.3, 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: 134, 11: 1, 12: 1, 13: 1, 1: 1, 15: 101}
>>> d
{2: 12.3, 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: 134, 11: 1, 12: 1, 13: 1, 1: 1, 15: 101}
>>> n=d.copy()
>>> n[13]=12
>>> n
{2: 12.3, 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: 134, 11: 1, 12: 1, 13: 12, 1: 1, 15: 101}
>>> d
{2: 12.3, 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: 134, 11: 1, 12: 1, 13: 1, 1: 1, 15: 101}
>>> d.setdefault(2)
12.3
>>> d.setdefault(20)
>>> d
{2: 12.3, 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: 134, 11: 1, 12: 1, 13: 1, 1: 1, 15: 101, 20: None}
>>> d.setdefault(30,70)
70
>>> d
{2: 12.3, 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: 134, 11: 1, 12: 1, 13: 1, 1: 1, 15: 101, 20: None, 30: 70}
>>> d{2: 12.3, 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 11: 1, 12: 1, 13: 1, 1: 1, 15: 101}
SyntaxError: invalid syntax
>>> 