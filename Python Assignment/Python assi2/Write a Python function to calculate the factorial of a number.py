def fact():
    # Take user input for a number and convert it to an integer
    n = int(input("Enter a number: "))
    
    # Initialize a variable 'factorial' with the value 1
    factorial = 1

    # Check if the entered number is greater than or equal to 1
    if n >= 1:
        # If true, execute a loop from 1 to n (inclusive)
        for i in range(1, n + 1):
            # Multiply 'factorial' by the loop variable 'i'
            factorial = factorial * i

    # Print the calculated factorial
    print("Factorial of the given number is:", factorial)

# Call the 'fact' function
fact()
