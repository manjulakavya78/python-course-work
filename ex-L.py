n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i == n-1 or   j==0  :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

