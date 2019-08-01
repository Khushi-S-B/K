def m1():            # method number 1
    def sum(a,b):
        c=a+b
        print(c)
    def mul(a,b):
        c=a*b
        print(c)
    sum(a,b)
    mul(a,b)
q=m1()
r=q[0]
t=q[1]
r=(1,2)
t=(4,5)

def m2():            # method number 2
    def sum(a,b):
        c=a+b
        return c
    def mul(a,b):
        c=a*b
        return c
    return sum,mul
f=m2() # comes as a tuple
s=f[0]
m=f[1]
s(1,2)
m(4,5)



    
    
