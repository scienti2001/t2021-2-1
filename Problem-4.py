#Initialization of value a
a = [1,2,3,4,5,6,7,8,9] 
#Map function for multiple input
b = map(int,input().split())
#Converting to list
b = list(b)
#Empty Dict c
c = {} 
#For loop with range a
for x in a:
    #count variable initialization
    count = 0
    #for loop with range b
    for y in b:
        #if loop
        if(y%x)==0:
            count=count+1
        else:
            #pass the case
            pass
        #update the dict c
        c.update({x:count})
print(c)