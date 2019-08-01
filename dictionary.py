x={1:"vanilla",2:"chocolate",3:"strawberry"}
for i in x:
    print(i, end=' ')
    print(x[i])
print()
x[4]='abcd'
x[5]='xyz'
x[1]='butterscotch'

print(x)

del x[1]
print(x)

y=list(x.items())
print(y)
