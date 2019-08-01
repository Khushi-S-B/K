key=int(input("Enter a number: "))
x=[3,4,8,7,1,2]
flag=0
for i in x:
    if i==key:
        flag=1
        break
if flag==1:
    print("Element found")
else:
    print("Element not found")
