li1=[]
li2=[]

no=int(input("enter your no"))

for no in range(10):
    if no%2==0:
        li1.append(no)
    else:
        li2.append(no)

print("even list",li1)
print("odd list",li2)
        
    
