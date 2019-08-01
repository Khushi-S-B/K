s='Betty bought some butter but the butter Betty bought was bitter so Betty bought some better butter to make the bitter butter better'

data = s.split(" ")
print(data)

for w in data:
    print(w," ",data.count(w))
