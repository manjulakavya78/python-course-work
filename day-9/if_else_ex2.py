t=('Laptop','Mobile','Watch')
print('Available Products:\nLaptop\nMobile\nWatch')
product=input("Search Products:")
if product in t:
    print("product found")
else:
    print("product not found")
