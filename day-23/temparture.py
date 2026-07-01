class temp:
    def __init__(self,celsius):
        self.celsius=celsius
    def to_f(self):
        print((self.celsius*9/5)+32)
    def to_c(self,f):
        print((f-32)*5/9)
t1=temp(25)
t1.to_f()
t1.to_c(70)
