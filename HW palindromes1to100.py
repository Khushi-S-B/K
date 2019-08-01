n=1
while n<=100:
    temp=n
    num=0
    while temp>0:
        r=temp%10
        temp=temp//10
        num=num*10+r
    if num==n:
        print(n)
    n=n+1    
