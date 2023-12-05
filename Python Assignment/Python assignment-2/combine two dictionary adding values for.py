'''
Write a Python program to combine two dictionary adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).
'''
d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':400,'d':400,'c':300}
d3={}

combined_dict = {}

for key in d1:
    if key in d2:
        # Add values for common keys
        combined_dict[key] = d1[key] + d2[key]
    else:
        # If the key is unique to dict1, add it to the combined dictionary
        combined_dict[key] = d1[key]

# Add keys from dict2 that are not in dict1
for key in d2:
    if key not in d1:
        combined_dict[key] = d2[key]

print(combined_dict)
