#Write a Python program to print all unique values in a dictionary.

# Example dictionary
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

# Using set to get unique values
unique_values_set = set(my_dict.values())

# Print the unique values
print("Unique values in the dictionary:", list(unique_values_set))

