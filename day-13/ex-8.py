n = int(input("Enter the size: "))

ch = 65  

for row in range(n):
    for col in range(n-row):
        print(chr(ch), end=' ')
        ch += 1
    print()
