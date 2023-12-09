'''
Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd

'''

# Sample data
sample_data = {1: ['a', 'b'], 2: ['c', 'd']}

# Use nested loops to generate and display all combinations
for letter_1 in sample_data[1]:
    for letter_2 in sample_data[2]:
        print(letter_1 + letter_2, end=' ')



