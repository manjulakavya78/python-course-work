'''
import re
pattern=r'[0-9]'
text='56227737 codegnan python version 3.11.4'
res=re.search(pattern,text)
print(res.group()if res else "pattern not found")
'''


import re
pattern=r'[a-z]'
text=' 2435636 codegnan python version 3.11.4'
res=re.search(pattern,text)
print(res.group()if res else "pattern not found")
