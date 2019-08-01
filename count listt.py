x=['hi','I','am' ,'a','human','huh','pup']
count=0
for i in x:
    if len(i)>=2:
        if i[0]==i[-1]:
            count=count+1
print(count)            
