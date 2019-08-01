for i in range(1,101):
    a=1
    count=0
    while(a<=i):
        if(i%a==0):
            count=count+1
        a+=1
            
    if(count==2):
        print(i)
