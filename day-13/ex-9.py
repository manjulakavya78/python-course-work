n = int(input("Enter the size: "))

 

for row in range(n):
    for sp in range(n-row-1):
        print(' ', end=' ')
    for col in range(row+1):
        print('*', end=' ')
     
    
     
    print()
