class aroftri:
    def init(self,base,height):
        self.base=base
        self.height=height
    def ar(self):
        self.area=0.5*self.base*self.height
    def display(self):
        print(self.area)
c=aroftri()
c.init(3,4)
c.ar()
c.display()
