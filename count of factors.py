i=int(input("Enter a number: "))
a=1
count=0
while a<=i:
      if i%a == 0:
          count+=1
      a=a+1
print(count)
