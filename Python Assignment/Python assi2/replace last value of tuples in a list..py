# Write a Python program to replace last value of tuples in a list.


list1=[(12,32,12),(12,'Nikhil',13)]

new=[]

for tup in list1:
    ntup = tup[:-1]+('good',)#replace the  last elements using slicing
    new.append(ntup)

print(new)
