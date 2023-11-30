# Write a Python program to convert a list of tuples into a dictionary.


li=[("one",1),("Two",2),("Three",3),("Four",4)]

di={}	

for i in li:

   di[i[0]]=i[1]

print(di)
