d={1:'a',2:'b',3:'c'}
d.setdefault(4,'d')# can only be used for non-existing keys
# can be modified in future
d[4]='e'
print(d)
