def display():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner functiom: ",n)
    inner()
    print("Outer function: ", n)
display()
