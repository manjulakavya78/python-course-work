'''
import re
pattern=r'[a-z]{5}'
text='asrtg'
res=re.fullmatch(pattern,text)
print(res.group() if res else "pattern not found")
'''

import re
pattern=r'[a-z]{4}'
text='asrtg'
res=re.fullmatch(pattern,text)
print(res.group() if res else "pattern not found")
