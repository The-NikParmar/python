'''
Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers
'''

decimal_numbers = [float(x) for x in input("Enter decimal numbers separated by spaces: ").split()]

# Using built-in functions to find maximum and minimum
maximum_number = max(decimal_numbers)
minimum_number = min(decimal_numbers)

print(f"The maximum number is: {maximum_number}")
print(f"The minimum number is: {minimum_number}")
