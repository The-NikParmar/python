# Write a Python program to get unique values from a list

# Create a list
li=[12,544,76,23,45,87,54,11,22,33,22,33,56]
# Create an  unique list
unique=[]

#check unique elements and append in unique list
for i in li:
    if i not in unique:
        unique.append(i)

print("The all elements list:- ",li)
print("unique value form list ",unique)
