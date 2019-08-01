
x=[(2,5),(1,2),(4,4),(2,3),(2,1)]
length=len(x)
for i in range(0,length):
    for j in range(i+1,length):
        t1=x[i]
        t2=x[j]
        if t1[1]>t2[1]:
            a=x[i]
            x[i]=x[j]
            x[j]=a
print(x)            
    
    
