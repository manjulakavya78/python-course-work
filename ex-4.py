n=int(input("Enter the size: "))
c=1
for row in range(n):
            for col in range(n):
                  print(str(c).zfill(2),end=' ')
                  c+=1
            print()
