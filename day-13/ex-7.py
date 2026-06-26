n = int(input("Enter the size: "))

ch = 65  

for row in range(n):
    for col in range(row + 1):
        print(chr(ch), end=' ')
        ch += 1
    print()
