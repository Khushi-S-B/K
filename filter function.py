x=[1,2,3,4,5]
# def isEven(x):
#      if x%2==0:
#          return True
#      else:
#          return False
y=list(filter(lambda i: i%2==0,x))# if we dont apply list then we will get
                                  # a boolean list such as [True,False,..]
print(y)
