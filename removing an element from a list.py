ERROR
x=[1,3,2,2]
n=2
l=len(x)
i=0
while(i<l):
    if(x[i]==n):
        x.remove(x[i])
    l=l-1
    i+=1
print(x)        
        
