
import re
pattern=r'h.t'
text='hat hot h@t H&t hat HoT'
res=re.findall(pattern,text)
print(res)
