x=([1,2,3,4,5])
for i in x:
    count=0
    a=1
    while a<=i:
        if i%a==0:
            count+=1
        a+=1    
    if count==2:
        print(i)
