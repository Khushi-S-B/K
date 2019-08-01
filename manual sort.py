x=[4,8,2,1,8]

for i in range(0,5):
    for j in range(i+1,5):
        if x[i]>x[j]:
            a=x[i]
            x[i]=x[j]
            x[j]=a
print(x)            
