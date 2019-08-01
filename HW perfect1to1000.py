n=1
while n<=1000:
    sum=0
    a=1
    while a<n:
        if n%a==0:
            sum=sum+a
        a=a+1    
    if sum==n:
        print(n)
    n=n+1
