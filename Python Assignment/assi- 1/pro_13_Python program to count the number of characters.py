st=input("enter your string")

cout={}
for i in st:
    if i in cout:
        cout[i]+=1
    else:
        cout[i]=1

print("the number of characters",cout)
