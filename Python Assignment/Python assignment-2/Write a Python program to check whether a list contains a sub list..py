# Write a Python program to check whether a list contains a sub list
li = [12, 32, 12, 342, 13, 12, 4, 5, 6]
li1 = [5, 12, 32]

counter = 0

# Check if each element in li1 is present in li
for i in li1:
    if i in li:
        counter += 1
    else:
        counter = 1  # If an element is not present, reset counter to 1

# Check if all elements in li1 were found in li
if counter == len(li1):
    print("yes")
else:
    print("no")
`
