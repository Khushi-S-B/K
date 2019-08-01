n=int(input("Enter a number: "))

while n>0:
    r=n%10
    n=n//10
    if r%2==0:
        print(r)
