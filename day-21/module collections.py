
'''
from collections import Counter,defaultdict,deque
s='python programming'
l=[1,1,2,3,45,6,3,4,56,8,91,9]
print(Counter(s))
print(Counter(l))


'''

'''
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
'''
'''
from collections import defaultdict,deque
s='python programming'
l=[1,1,2,3,45,6,3,4,56,8,91,9]
d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)
    
'''
from collections import deque
d=deque([])
d.append(10)
d.append(20)
d.append(30)
d.popleft()
d.popleft()
d.append(50)
d.append(70)
d.popleft()
print(d)
