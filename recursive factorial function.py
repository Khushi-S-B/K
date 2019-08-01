def factorial(a):
    if a==1:
        return 1
    else:
        fact=a*factorial(a-1)
    return fact    
print(factorial(3))        
