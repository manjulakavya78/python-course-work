import re
pattern=r'^0|\+91'
text='+91876543212'
res=re.findall(pattern,text)
print(res)
