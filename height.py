students=input("Input of list").split()
for n in range(0,len(students)):
    students[n]=int(students[n])
print(students)

total=sum(students)
num=len(students)
avg=round(total/num)
print(avg)