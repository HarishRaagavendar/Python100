import random
namesstring=input("The persons who are coming on")
names=namesstring.split(',')
print(names)
items=len(names)
ch=random.randint(0,items-1)
pay=names[ch]
print(pay)
