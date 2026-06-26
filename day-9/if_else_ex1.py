credentials=('admin','admin@123')
uname=input("Username:")
pwd=input("password:")
if (uname,pwd)==credentials:
    print("Login Successful")
else:
    print("Invalid Credentials")
