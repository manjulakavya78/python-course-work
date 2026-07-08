import re
pattern=r'^[6-9]'
text='987654321'
res=re.findall(pattern,text)
print(res)
