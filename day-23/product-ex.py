class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def given_discount(self,percent):
        self.price-=self.price*(percent/100)
    def display_price(self):
        print(f"Discount price:{self.price}")
p1=Product("mobile",40000)
p1.given_discount(10)
p1.display_price()
