n = int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or (i==m and j<=m) or ( i+j==n-1 and i<=m) or (i==j and  i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
