n=int(input("Enter a number: "))
sum=0
while n>0:
    r=n%10
    n=n//10
    a=1
    count=0
    while a<=r:
        if r%a == 0:
            count+=1
        a=a+1
    if count==2:
        sum+=r
print(sum)
