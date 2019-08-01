i=int(input("Enter a number: "))
a=1
sum=0
while a<=i:
      if i%a == 0:
          sum+=a
      a=a+1
print(sum)    
