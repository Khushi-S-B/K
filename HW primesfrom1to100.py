n=1
while n<=100:
    s=1
    count=0
    while s<=n:
        if n%s==0:
            count+=1
        s+=1
    if count==2:
        print(n)
    n+=1
