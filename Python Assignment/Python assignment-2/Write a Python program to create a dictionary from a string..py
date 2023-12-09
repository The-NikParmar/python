#Write a Python program to create a dictionary from a string.

string = 'w3resource'

# empty dictionary to store letter counts
letter_count_dict = {}

# Iterate through each character in the string
for letter in string:
    if letter in letter_count_dict:
        letter_count_dict[letter] += 1
    else:
        letter_count_dict[letter] = 1

# Print the result
print(letter_count_dict)
