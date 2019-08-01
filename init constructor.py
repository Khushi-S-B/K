class Car:
    def __init__(self,name,model):        self.name=name
        self.model=model
    def display(self):
        print(self.name)
        print(self.model)
c=Car("abc",2015)
c.display()
