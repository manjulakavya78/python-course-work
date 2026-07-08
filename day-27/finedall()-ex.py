import re
pattern=r'[a-z]'
text=' 2435636 codegnan python version 3.11.4'
res=re.findall(pattern,text)
print(res)
