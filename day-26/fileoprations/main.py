'''
file=open('sample.txt','r')
print(file.read())
file.seek(2)
print(file.readlines())
file.seek(1)
print(file.readlines())
file.close()
'''
with open('sample.txt','r') as file:
    print(file.read())
    file.seek(2)
    print(file.readlines())
    file.seek(1)
    print(file.readlines())
    file.close()
