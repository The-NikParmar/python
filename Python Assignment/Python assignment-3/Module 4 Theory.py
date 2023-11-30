'''
Q-1 What is File function in python? What is keywords to create and write
file.


In Python, there is no specific "File function." Instead, the term typically
refers to
various functions and methods related to file manipulation and I/O operations
provided by the Python standard library.The key function for working with files
is open().

The open() function is used to open a file and create a file object, which can
then be used for various file-related operations, such as reading, writing,
or appending data.

In Python, the open() function is used to create or open a file, and the write()
method is used to write data to the file.

Example of file create and write

with open('Que1.txt', 'w') as file:
    file.write('Hello, World!')

==================================================================================
Q-13 Explain Exception handling? What is an Error in Python?

Exception handling in Python is a mechanism that allows a program to deal with errors 
or exceptional situations gracefully rather than abruptly terminating. 
Errors in Python are represented as exceptions. When an error occurs during the execution of a program,
an exception is raised, and the program flow is interrupted.

Here are the key components of exception handling in Python:

Try: The try block encloses the section of code where an exception might occur. 
It's the segment of code that you want to monitor for errors.

Except: The except block follows the try block and specifies the code that should be executed if a specific exception occurs.
You can have multiple except blocks to handle different types of exceptions.

Else: The else block contains code that is executed if the try block does not raise an exception. It's optional.

Finally: The finally block contains code that is always executed, whether an exception occurred or not. 
It's optional but commonly used for cleanup operations.



An "error" in Python generally refers to a situation where the program cannot proceed as intended due to unexpected conditions.
Errors can be broadly categorized into two types:

Syntax Errors: These are errors that occur when the Python interpreter encounters invalid Python code. 
They are detected during the parsing of the code and prevent the program from running.

Example:
print("Hello, world!"

Runtime Errors (Exceptions): These errors occur during the execution of the program. 
They are not detected by the interpreter until the program is run.

=======================================================================================
Q-14 How many except statements can a try-except block have? Name Some
built-in exception classes:

A try block in Python can have multiple except blocks to handle different types of exceptions.

The general syntax is as follows:

try:
    # Code that might raise an exception
except ExceptionType1:
    # Handle ExceptionType1
except ExceptionType2:
    # Handle ExceptionType2
# ...
except ExceptionTypeN:
    # Handle ExceptionTypeN
else:
    # Code to execute if no exception occurred
finally:
    # Cleanup code (always executed)

1:- ZeroDivisionError: Raised when division or modulo by zero occurs.
2:- ValueError: Raised when a function receives an argument of the correct 
    type but with an invalid value.
3:- FileNotFoundError: Raised when an attempt to open a file or directory 
    fails because it does not exist.

===========================================================================================
Q-15 When will the else part of try-except-else be executed?


The else part of a try-except-else block in Python is executed when no exceptions 
are raised in the try block. If any exception occurs, the control will transfer to 
the corresponding except block, and the else block will be skipped.

Example:-

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful. Result:", result)


Example:- 

In this example, if the division operation in the try block succeeds (no division by zero), the else block will execute, 
and the successful result will be printed. If a ZeroDivisionError occurs, the corresponding except block will be executed, 
and the message about division by zero will be printed.

=============================================================================================
Q-16 Can one block of except statements handle multiple exception?


Yes, a single except block in Python can handle multiple exceptions. 
You can provide a tuple of exception types or use a common base class to
catch multiple types of exceptions in a single except block.

Here are two ways to handle multiple exceptions:

Using a Tuple of Exception Types:

try:
    # Code that might raise an exception
except (ExceptionType1, ExceptionType2, ..., ExceptionTypeN) as e:
    # Handle the exceptions

Using a Common Base Class:

You can catch multiple exceptions by using a common base class for those exceptions. 
All exceptions derived from the base class will be caught.

try:
    result = int("abc")
except (ValueError, TypeError) as e:
    print(f"An exception occurred: {str(e)}")
================================================================================================

Q-17 When is the finally block executed?

Always Executed: The finally block is always executed after the try block, 
regardless of whether an exception is raised or not.

Cleanup Operations: It is commonly used for cleanup operations such as closing files, 
releasing resources, or cleaning up temporary variables.

Useful for Resource Management: If you open a file or acquire a resource in the try block,
the finally block ensures that the file is closed or the resource is released, even if an 
exception occurs.
'''

