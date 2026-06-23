n = int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==n-1 or i==0 or (j==0 and i<=m) or (j==n-1 and i>=m) or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
