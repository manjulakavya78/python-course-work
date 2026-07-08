'''
import re
pattern=r'[A-Z]'
text='Codegnan'
res=re.match(pattern,text)
print(res.group()if res else "pattern not found")
'''



import re
pattern=r'[A-Z]'
text='codegnan'
res=re.match(pattern,text)
print(res.group()if res else "pattern not found")

