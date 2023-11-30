#Write a Python program to find the maximum and minimum numbers from the specified decimal numbers

decimal_numbers = [3.14, 2.71, 5.55, 1.23, 4.0]

# Check if the list is not empty
if decimal_numbers:
    
    # Initialize max and min with the first element of the list
    max_number = min_number = decimal_numbers[0]

    for num in decimal_numbers:
        # Update max_number if a larger number is found
        if num > max_number:
            max_number = num
        # Update min_number if a smaller number is found
        elif num < min_number:
            min_number = num
            
    print(f"The maximum value is: {max_number}")
    print(f"The minimum value is: {min_number}")

else:
    print("The list is empty.")
