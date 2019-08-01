n=int(input("Enter a number: "))
a=n
sum=0
while a>0:
    r=a%10
    sum=sum*10+r
    a=a//10
if sum==n:
    print("Palindrome")
else:
    print("not a palindrome")
    
