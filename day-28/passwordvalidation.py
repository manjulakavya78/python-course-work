import re
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
password = input("Enter the password: ")
res = re.fullmatch(pattern,password)
print("Valid password" if res else "Invalid password")
