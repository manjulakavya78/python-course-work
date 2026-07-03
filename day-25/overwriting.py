class number:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return self.n+other.n
    def __sub__(self,other):
        return self.n-other.n
    def __mul__(self,other):
        return self.n*other.n
    def __truediv__(self,other):
        return self.n/other.n
    def __gt__(self,other):
        return self.n>other.n
    def __lt__(self,other):
        return self.n<other.n
    def __eq__(self,other):
        return self.n==other.n
    def __str__(self):
        return str(self.n)
a=number(20)
b=number(10)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a>b)
print(a<b)
print(a==b)
print(a,b)

    
