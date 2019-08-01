s1={1,2,3,4}
s2={3,4,5,6}
x=s1.union(s2)
print(x)

y=s1.intersection(s2)
print(y)

s1.intersection_update(s2)
print(s1)
print(s2)
