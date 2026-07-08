import re
pattern = r'^[A-Za-z]{2,15} ( [A-Za-z]{2,15})+$'
name = input("Enter the name:")
res = re.fullmatch(pattern,name)
print("Valid name" if res else "Invalid name")
