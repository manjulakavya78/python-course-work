n = int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
