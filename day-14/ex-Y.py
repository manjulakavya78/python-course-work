n = int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and j<=m) or (i+j==n-1 and j>=m) or (j==m and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


