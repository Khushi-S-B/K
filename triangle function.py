def triangle_pattern(n):
    for i in range(0,n):
        j=0
        while j<=i:
            print("*",end=' ')
            j+=1
        print()
triangle_pattern(8)        
