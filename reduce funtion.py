from functools import*
x=[1,2,3,4,5]

#def add(a,b):
#     c=a+b
#     return c #after getting c, the next two args are 3(c) and 3(next ele in list)

l=reduce(lambda a,b:a+b,x)#reduce can only work with functions with 2 args
print(l)
