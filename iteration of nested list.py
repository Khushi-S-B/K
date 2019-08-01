x=[1,2,3,4,5,6,[8,9,10],6,7,8]
ind=0
for i in x:
    if type(i)==list:
        ind=x.index(i)
print(x[0:ind])            
    
