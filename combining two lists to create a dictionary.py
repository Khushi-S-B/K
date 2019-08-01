keys=[1,2,3,4]          # sizes of the list must be same otherwise it ignores 
values=['a','b','c','d']# the remaining keys, values or num
num=['w','x','y','z']
d={}
for k,v,n in zip(keys,values,num):
    s=v+n
    d[k]=s
    print
print(d)    
