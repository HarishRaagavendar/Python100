n=int(input("Enter the num: "))
bin=''
while n>0:
    r=n%2
    n=n//2
    bin=str(r)+bin


print(bin)
    