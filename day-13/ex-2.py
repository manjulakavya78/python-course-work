n=int(input("Enter the size: "))
for row in range(n):
            for col in range(n):
                  print(int(row+col>=n-1),end=' ')
            print()
