n=int(input("Enter a number: "))
a=n
sum=0
while a>0:
    r=a%10
    a=a//10
    sum=sum+(r**3)
if sum==n:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
