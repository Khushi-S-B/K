

def dec(hello):
    def inner(name):
        if name=="momo":
            print("Go away")
        else:
            hello(name)
    return inner
@dec
def hello(name):
    print("Hi",name,"!")

hello("Laurie")


    
