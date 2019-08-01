def sum(n):
    if n==1:
        return 1 #because when n is 1, only 'if' part will execute and then value
    # will be returned and after 'return' the code won't run
    else:                     # do we really need the else here? Ans: we don't
        s=n+sum(n-1)
    return s
print(sum(10))

