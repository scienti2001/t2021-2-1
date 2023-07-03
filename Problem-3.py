#Input the value of a
a = int(input("Enter the value of a"))

#If Case
if a%2==0:
    a-=1

#Empty List
b=[]
#Count Initialise to -1
c=-1

#For Loop for printing the series
for i in range(a):
    c+=2
    b.append(c)
print(*b)