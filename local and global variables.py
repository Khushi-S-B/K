# code to learn local and global variables    
b=2
def f1():
    global a
    a=20
    print(a)
def f2():
    global a
    a=40
    print(a)    
def f3():
    a=50
    b=1
    print(a)
    print(globals()['a'])# cannot put comma and add 'b'
    print(globals()['b'])
f1()
f2()
f3()
