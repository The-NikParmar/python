'''
Write a Python function that checks whether a passed string is
palindrome or not
'''

def palindrome(string):

    if string[0] == string[-1]:
        # Check if the first and last characters of the string are the same.
        print("String is a palindrome.")
    else:
        print("String is not a palindrome.")

# Taking user input for the string
input_string = input("Enter a string: ")
# Asks the user to input a string.

palindrome(input_string)
# Calls the 'palindrome' function with the user-inputted string.

    

