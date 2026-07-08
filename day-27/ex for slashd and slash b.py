'''
import re
pattern=r'\d\b'
text='a 12 b 13 c 14 d 15 e 16 f 18'
res=re.findall(pattern,text)
print(res)

'''
'''import re
pattern=r'\d{2}\b'
text='a 12 b 13 c 14 d 15 e 16 f 18'
res=re.findall(pattern,text)
print(res)
'''
'''
import re
pattern=r'\D'
text='a 12 b 13 c 14 d 15 e 16 f 18'
res=re.findall(pattern,text)
print(res)

'''
'''
import re
pattern=r'\w'
text='a 12 b 13 c 14 d 15 e 16 f 18'
res=re.findall(pattern,text)
print(res)
'''
'''

import re
pattern=r'\W'
text='a 12 b 13 c 14 d 15 e 16 f 18'
res=re.findall(pattern,text)
print(res)
'''
'''
import re
pattern=r'\s'
text='a 12 b 13 c 14 d 15 e 16 f 18'
res=re.findall(pattern,text)
print(res)
'''
import re
pattern=r'\S'
text='a 12 b 13 c 14 d 15 e 16 f 18'
res=re.findall(pattern,text)
print(res)

