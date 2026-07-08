import re
pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = input("Enter the email:")
res = re.fullmatch(pattern,email)
print("Valid email" if res else "Invalid email")
