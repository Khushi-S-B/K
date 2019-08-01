ERROR
a=(3,6,5,8,1,2,1,1,2,5,4,4)
x=list(a)
y=[]
for i in x:
    if i not in y:
        y.append(i)
    print(i, x.count(i))        
        
    
