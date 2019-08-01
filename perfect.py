i=int(input("Enter a number: "))
sum=0
a=1
while a<i:
      if i%a==0:
          sum+=a
      a+=1
if sum==i:
      print("It is a perfect number")
else:
      print("It is not a perfect number")
      
