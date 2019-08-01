d={}
keys=[1,2,3]
values=1,2,3#here, 'values' is treated as a tuple of (1,2,3),even if u put brackets
d1=d.fromkeys(keys,values)
print(d1)
# in python, a single value can be assigned multiple values which is treated as
#a single tuple
# in python, we cannot add values and keys together as a list, it can only be
# done through indexing such as d[1]=1
