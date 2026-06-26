n = int(input("Enter the size: "))

 

for row in range(n):
    for sp in range(row):
        print(' ', end=' ')
    for col in range(n-row):
        print('*', end=' ')
     
    
     
    print()
