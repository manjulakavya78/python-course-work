with open('sample.txt','a+')as file:
    file.write("Open.   Close.  Write.   Read")
    file.seek(0)
    print(file.read())
