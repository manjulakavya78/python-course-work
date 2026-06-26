n = int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
