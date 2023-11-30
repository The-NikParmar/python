'''
How Do You Handle Exceptions With Try/Except/Finally In Python?
Explain with coding snippets.


Handling exceptions in Python using try, except, and finally blocks
allows you to gracefully manage errors and ensure that necessary
cleanup operations are performed.
Here are coding snippets to illustrate how to use try, except, and finally:
'''

try:
    # Code that might raise an exception
    result = 10 / 0  # Division by zero to trigger an exception
except ZeroDivisionError:
    # Handle specific exception
    print("Cannot divide by zero.")
except Exception as e:
    # Handle other exceptions
    print(f"An error occurred: {str(e)}")
else:
    # Code to execute if no exception occurred
    print("Division successful.")
finally:
    # Cleanup code (always executed)
    print("Cleanup operations.")
