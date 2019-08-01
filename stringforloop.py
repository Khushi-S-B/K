s='emma'
for n in s:
    print(n)
for n in s[::-1]:
    print(n)
for n in range(0,len(s)):#there is no need to put n-1 as, if length is 7 then
    print(s[n])                     # automatically n-1 (6) is taken
for i in range(len(s)-1,-1,-1): # if length is 8 ,but the string is numbered as
    print(s[i])                 # 0,1,2,...7 so we have to start with 7 so we
                                # do len(s)-1
