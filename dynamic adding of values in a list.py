s=set()
p=set([1,2,3])
for i in range(1,4):
    x=int(input("Enter a number: "))
    s.add(x)
print(s)
s.update(p)
print(s)
