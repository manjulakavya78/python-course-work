import re
pattern=r'[a-z]'
text='codegnan python version 3.11.4'
res=re.match(pattern,text)
print(res.group()if res else "pattern not found")

