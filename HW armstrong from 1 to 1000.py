
n=1
while n<=1000:
    temp=n
    sum=0
    while temp>0:
        r=temp%10
        temp=temp//10
        sum=sum+(r**3)
    if sum==n:
        print(n)
    n=n+1    
