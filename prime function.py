def isPrime(a):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
s=isPrime(8)
if (s): # can also put s==True
    #because True==True is True
    #and False==True is False
    print("Prime")
else:
    print("Composite")

