i=int(input("Enter a number: "))
a=1
count=0
while a<=i:
      if i%a == 0:
          count+=1
      a=a+1
if count==2:
    print("It is a prime number")
elif count>2:
    print("It is a composite number")
elif count<2:
    print("It is neither prime nor composite")
