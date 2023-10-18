li1=[]
el=int(input("how many elements insert"))

for  i in range(0,el):
    
     no=int(input("enter your elements"))

     li1.append(no)


for i in range(len(l1)):
    for j in range(i+1,len(l1)):

        if li1[i]<li1[j]:
            li1[i],li[j]=li[j],li1[i]

print(li1)

    
