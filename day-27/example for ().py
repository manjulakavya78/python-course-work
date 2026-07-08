import re
pattern=r'(abc)'
text='abcd abc abderf abdecsss'
res=re.findall(pattern,text)
print(res)
