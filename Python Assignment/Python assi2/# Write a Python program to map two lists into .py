# Write a Python program to map two lists into a dictionary

def mapping(x, y):
    return x, y

li1 = [1, 2, 3, 4, 5]
li2 = ['nik', 'smit', 'mohit', 'krishna', 'jerry']

# Use the map function to apply the mapping function to corresponding elements of the lists
# Convert the result to a dictionary
result_dict = dict(map(mapping, li1, li2))

print(result_dict)
