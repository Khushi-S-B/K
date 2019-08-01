x=[1,2,3,4,5]
a=0
for i in x:
    x[a]=i+100
    a=a+1
print(x)

y=list(map(lambda i:i+100,x)) # we can also create a separate function
