def outer():
    def add(a,b):
        s=a+b
        print("Sum:",s)
    def subtract(a,b):
        d=a-b
        print("Difference:",d)
    def multiply(a,b):
        p=a*b
        print("Product:",p)
    def divide(a,b):
        q=a//b
        print("Quotient:",q)
    return add,subtract,multiply,divide
    print("done!")
a=outer()
b=a(2,3)
f1=b[0]()
f2=b[1]()
f3=b[2]()
f4=b[3]()

