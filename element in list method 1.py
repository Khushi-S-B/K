key=int(input("Enter a number: "))
x=[3,4,8,7,1,2]

for i in x:
    if i==key:
        print("Element found")
if key not in x:
        print("Element not found")
