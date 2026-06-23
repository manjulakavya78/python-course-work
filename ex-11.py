n = int(input("Enter the size: "))
m=n//2
for row in range(n):
    if row<=m:
        for col in range(row+1):
            print('*',end=' ')
    else:
        for col in range(n-row):
            print('*',end=' ')
    print()
