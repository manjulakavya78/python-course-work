import re
pattern = r'^(?:\+91|10)?[6-9]\d{9}$'
phnno = input("Enter the phnno: ")
res = re.fullmatch(pattern,phnno)
print("Valid phnno" if res else "Invalid phnno")
