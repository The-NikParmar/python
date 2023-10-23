li=["abc","xyx","neel","smit"]

counter=0

for i in li:
    if len(i)>1 and i[0]==i[-1]:
        counter+=1

print(li)
print(counter)
        
