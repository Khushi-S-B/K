def outer():
    print("outer function")
    def inner():
        print("inner function")
    inner()#u cannot make a call to inner func without calling outer
    print("done")
    return inner
a=outer()    # a FUNCTION is returned
print(a)     # address of the function is given
a()          # returns the output of inner function
