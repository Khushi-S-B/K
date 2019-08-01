#ERROR
class Counter:
    #static/class variable
    x=10
    def incr():
        Counter.x=Counter.x+1
        print(Counter.x)
c1=Counter()
c2=Counter()
c1.incr()
c2.incr()

class Pet:
    @classmethod
    def incr(cls):
        Counter.x=Counter.x+1
        print(Counter.x)
c1=Counter()
c2=Counter()
c1.incr()
c2.incr()


