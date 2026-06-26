def display():
    course='Java FullStack'
    print("Starting:",course)
    def change():
        nonlocal course
        course='python FullStack'
        print("Updated:",course)
    change()
    print("Final Course:",course)
display()
