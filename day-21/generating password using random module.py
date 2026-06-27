import random
name=input("Enter the name:")
spe_chars=['!','@','#','$','^','&','*']
sample1=random.choices(name,k=4)+random.choices(spe_chars,k=2)
sample2=(''.join(sample1)).title()
print(sample2+str(random.randint(1111,9999)))
