import re
pattern=r'\.py'
text='main.py'
res=re.findall(pattern,text)
print(res)
