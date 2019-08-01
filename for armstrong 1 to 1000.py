
for n in range(1,1001):
    temp=n
    sum=0
    while temp>0:
        r=temp%10
        temp=temp//10
        sum=sum+(r**3)
    if sum==n:
        print(n)
        
