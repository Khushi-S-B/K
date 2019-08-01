class Person:
    def setData(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)
p1=Person()
p2=Person()
p1.setData("Mi",25,"Female")
p1.display()
p2.setData("Ish",14,"Male")
p2.display()
              
