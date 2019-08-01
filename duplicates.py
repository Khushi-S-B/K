ori=[1,1,2,3,3,3,4,4,5]
new=[]
for i in ori:
    if i not in new:
        new.append(i)
print(ori)
print(new)
