
import re
pattern=r'[0-9]'
text='abc 12 def 34 ghi 56 jkl 67 mno 78 opq 89 rst 90 '
res=re.sub(pattern,'*',text)
print(res)
