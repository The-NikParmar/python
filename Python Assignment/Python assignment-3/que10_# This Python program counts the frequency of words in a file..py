#Write a Python program to count the frequency of words in a file.

# This Python program counts the frequency of words in a file.

# Get the name of the file from the user.
file_name = input("Enter the name of the file: ")

# Open the file.
with open(file_name, "r") as file:
    # Read the contents of the file.
    words = file.read().split()
    
# Initialize a dictionary to store the word frequencies.
word_frequencies = {}

# Iterate over the words in the list.
for word in words:
    # If the word is already in the dictionary, increment the count.
    if word in word_frequencies:
        word_frequencies[word] += 1
    # Otherwise, add the word to the dictionary with a count of 1.
    else:
        word_frequencies[word] = 1

# Print the word frequencies.
for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")
