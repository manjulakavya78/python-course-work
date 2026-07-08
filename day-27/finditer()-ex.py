import re
pattern=r'[a-z]'
text=' 2435636 codegnan python version 3.11.4'
res=re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())
