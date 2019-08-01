ori=[1,2,5,3,8,7,4,4,3,5,1,1,1,9,0,2]
unique=[]

for n in ori:            # If you have a basket of apples of different sizes, &
    if n not in unique:  #and you must take only one of each size, then everyti-
        unique.append(n) #me you take an apple from the first basket, you must 
print(ori)               # check if there is already an apple of the same size      
print(unique)            # in the second basket. If not, only then you must add
                         # it
for w in unique:                # Here, w is a dummy variable and can be used
    print(w," ", ori.count(w))  # again
