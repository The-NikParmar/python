# Write a Python program to unzip a list of tuples into individual lists.

list_of_tuple = [(12,32),(45,345),(22,82),(56,86)]

li1=[]
li2=[]

for i in list_of_tuple:
    li1.append(i[0]) #individual list and unzip list of tuples
    li2.append(i[1])

print("orignal",list_of_tuple)
print("individual list1",li1) #list1 individula
print("individual list2",li2) #list2 individual

