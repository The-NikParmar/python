# Write a Python program to find the repeated items of a tuple.

tup = (1,2,3,2,3,4,5,1,6)

li=[]

repeted=[]

for i in tup:
    if i not in li:
        li.append(i)
    else:
        repeted.append(i)

print("orignal Tuple",tup)
print("repeted Elements",repeted)
