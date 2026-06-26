Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=set()
>>> s
set()
>>> s={1,2,3,4,5,5}
>>> s
{1, 2, 3, 4, 5}
>>> s
{1, 2, 3, 4, 5}
>>> s={1,4,5,3284,5667,352,223}
>>> s
{352, 1, 5667, 4, 5, 3284, 223}
>>> s+{1,2}
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s+{1,2}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> s*2
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s*2
TypeError: unsupported operand type(s) for *: 'set' and 'int'
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> s[1:2]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s[1:2]
TypeError: 'set' object is not subscriptable
>>> 1 in s
True
>>> 8 in s
False
>>> 18 not in s
True
>>> s=set
>>> s=set()
>>> s.add(1)
>>> s.add(12.4)
>>> s.add(2+3j)
>>> s.add('add')
>>> s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
>>> s.add((1,2,3,4))
>>> s.add({1,3,34,78})
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.add({1,3,34,78})
TypeError: unhashable type: 'set'
>>> s
{1, (2+3j), 12.4, (1, 2, 3, 4), 'add'}
>>> hash(10)
10
>>> hash('str')
5090477262521890027
>>> hash(1)
1
>>> girls={'kavya','pandu','pravallika','sruthi'}
>>> boys={'sreedhar','venky','sumu','ramana'}
>>> toppers={'hdh','djjieimd','venky'}
>>> girls | boys
{'pravallika', 'venky', 'ramana', 'sruthi', 'sumu', 'pandu', 'kavya', 'sreedhar'}
>>> girls & boys
set()
>>> topper & boys
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    topper & boys
NameError: name 'topper' is not defined
>>> toppers & boys
{'venky'}
>>> boys - toppers
{'sumu', 'ramana', 'sreedhar'}
>>> boys ^ toppers
{'ramana', 'sumu', 'djjieimd', 'hdh', 'sreedhar'}
>>> boys
{'sumu', 'venky', 'ramana', 'sreedhar'}
>>> {'venky'}>=boys
False
>>> a={1,2,4,5,3,6,7}
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> a>={1,2,3,4,5}
True
>>> {1,2,3,4,5}<=a
True
>>> {1,2,3,4,5}>=a
False
>>> girls.isdisjoint(toppers)
True
>>> boys.isdisjoint(toppers)
False
>>> boys.add(krishna)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    boys.add(krishna)
NameError: name 'krishna' is not defined
>>> boys.add("krishna")
>>> boys
{'venky', 'ramana', 'sumu', 'krishna', 'sreedhar'}
>>> boys.update('nivas','sree','lalith')
>>> boys
{'a', 'v', 'r', 'venky', 'ramana', 's', 'sumu', 'n', 'i', 't', 'h', 'krishna', 'l', 'e', 'sreedhar'}
>>> boys.update({'nivas','sree','lalith'})
>>> boys
{'a', 'v', 'r', 'venky', 'ramana', 's', 'lalith', 'sumu', 'n', 'i', 't', 'h', 'nivas', 'krishna', 'sree', 'l', 'e', 'sreedhar'}
>>> boys.update({'nivas','sree','lalith'})
>>> boys
{'a', 'v', 'r', 'ramana', 'sumu', 't', 'sree', 'sreedhar', 'lalith', 'venky', 's', 'n', 'i', 'h', 'nivas', 'krishna', 'l', 'e'}
>>> boys.update({'nivas','sree','lalith'})
>>> boys
{'a', 'v', 'r', 'ramana', 'sumu', 't', 'sree', 'sreedhar', 'lalith', 'venky', 's', 'n', 'i', 'h', 'nivas', 'krishna', 'l', 'e'}
>>> boys.pop()
'a'
>>> boys.remove('ramana')
>>> boys
{'v', 'r', 'sumu', 't', 'sree', 'sreedhar', 'lalith', 'venky', 's', 'n', 'i', 'h', 'nivas', 'krishna', 'l', 'e'}
>>> boys.remove('venky')
>>> boys
{'v', 'r', 'sumu', 't', 'sree', 'sreedhar', 'lalith', 's', 'n', 'i', 'h', 'nivas', 'krishna', 'l', 'e'}
>>> boys.update({'raju','gopi'})
>>> boys
{'v', 'r', 'sumu', 't', 'sree', 'raju', 'sreedhar', 'lalith', 's', 'n', 'i', 'h', 'nivas', 'krishna', 'l', 'gopi', 'e'}
>>> boys.discard('raju')
>>> boys
{'v', 'r', 'sumu', 't', 'sree', 'sreedhar', 'lalith', 's', 'n', 'i', 'h', 'nivas', 'krishna', 'l', 'gopi', 'e'}
>>> boys.clear()
>>> boys
set()
>>> boys={'venky', 'ramana', 'sumu', 'krishna', 'sreedhar'}

>>> boys
{'venky', 'ramana', 'sumu', 'krishna', 'sreedhar'}
>>> sorted(boys)
['krishna', 'ramana', 'sreedhar', 'sumu', 'venky']
>>> max(boys)
'venky'
>>> min(boys)
'krishna'
>>> len(boys)
5
>>> f=frozenset({1,2,3,4,5})
>>> f
frozenset({1, 2, 3, 4, 5})
>>> len(f)
5
>>> max(f)
5
>>> min(f)
1
>>> 