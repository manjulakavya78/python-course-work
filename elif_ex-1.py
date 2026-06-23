budget=int(input("Enter the budget:"))
if budget>10000:
    print('plan:Trip')
elif budget>5000:
    print('Resort Stay')
elif budget>3000:
    print('Movie and Dinner')
elif budget>1000:
    print('cafe and Shopping')
elif budget>500:
    print('Stret food and park visit')
else:
    print('Stay home')
