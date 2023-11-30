'''
Write python program that user to enter only odd numbers, else will
raise an exception.
'''

try:
    # Infinite loop until a valid odd number is entered
    while True:
        no = int(input("Enter an odd number: "))
        # Check if the number is odd
        if no % 2 == 1:
            print("You entered an odd number. Well done!")
            break  # Exit the loop if a valid odd number is entered
        else:
            ("Please enter only odd numbers.")
    
except ValueError as e:
    # Handle the exception
    print("Please enter only odd numbers.")
finally:
    print("Program execution complete.")
