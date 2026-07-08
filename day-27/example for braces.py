import re
pattern=r'[a-z]{2,6}'
text='ancd scv gagussn kkkwm sjsjw'
res=re.findall(pattern,text)
print(res)
