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

===================================================================================================
Q-21 What are oops concepts? Is multiple inheritance supported in java

In Python, "OOP" stands for Object-Oriented Programming, and it is a programming 
paradigm that uses objects and classes for structuring and organizing code.

 The main concepts in OOP are:
 1 class
 2 inheritance
 3 object
 4 Abstraction
 5 plymorephisam
 6 Encapsulation

 ====Is multiple inheritance supported in java====


No, Java does not support multiple inheritance through classes. 
In Java, a class can only directly extend one superclass. 
This was a design choice made to avoid certain complications 
and ambiguities associated with multiple inheritance, such as 
the "diamond problem."

=======================================================================================================
Q-22 How to Define a Class in Python? What Is Self? Give An Example Of
A Python Class.


In Python, a class is a blueprint for creating objects. Objects are instances of a
class, and each object can have attributes (characteristics) and methods (functions)
associated with it. The class defines the structure of the objects, encapsulating
data and behavior. Here's a basic overview of how to define a class in Python:


Class Declaration:-

To define a class, you use the class keyword, followed by the class name.Conventionally,
class names in Python use CamelCase.

========What is self?=========

In Python, self is a convention and not a reserved keyword. It is used as the first
parameter in the method definition within a class, representing the instance of the
class. The purpose of self is to reference the instance of the class and allows you
to access its attributes and methods.

************Example of Class*******************

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing attributes and calling methods
print(f"My dog's name is {my_dog.name} and it is {my_dog.age} years old.")
my_dog.bark()  # Output: Buddy says Woof!

======================================================================================
Que 26:- Explain Inheritance in Python with an example? What is init? Or What
Is A Constructor In Python?

Inheritance is a fundamental concept in object-oriented programming that allows a
new class (subclass/derived class) to inherit attributes and methods from an
existing class (superclass/base class). The subclass can then extend or override
the inherited properties. This promotes code reusability and supports the creation
of a hierarchy of classes.
=================
In Python, __init__ is a special method, often referred to as the "constructor.
"It is automatically called when an object is created from a class.
=================
In Python, a constructor is a special method called __init__ that is automatically
executed when an object is created from a class. 
=============================================================================================
Que:- 27 What is Instantiation in terms of OOP terminology

Instantiation, in the context of object-oriented programming (OOP), refers to the
process of creating an instance or object of a class. An instance is a specific
realization of a class, and it has its own set of attributes and methods based on
the class blueprint. When you instantiate a class, you create a unique object that
can be used to access and manipulate the attributes and methods defined in that
class.

====================In simpler terms:==========================

Class:

A class is a blueprint or template that defines the structure and behavior
of objects.
Object/Instance:

An object or instance is a concrete occurrence created from a class.
It represents a specific entity with its own set of characteristics.
Instantiation:

Instantiation is the process of creating an instance of a class.
It involves calling the class constructor (often __init__ in Python)
to initialize the attributes of the object.
========================================================================
Que:-28 What is used to check whether an object o is an instance of class A?

In Python, you can use the isinstance() function to check whether an object
is an instance of a particular class.

class A:
    pass

# Creating an instance of class A
obj = A()

# Checking if obj is an instance of class A
if isinstance(obj, A):
    print("obj is an instance of class A")
else:
    print("obj is not an instance of class A")
=====================================================================================
Que 29 :-What relationship is appropriate for Course and Faculty?

A professor can teach many courses, and a course can have many professors.
A course can also be offered on different schedules, with each offering taught
by a different professor. This relationship could be many-to-many.
==================================================================================================
Qur 30:-What relationship is appropriate for Student and Person?

The appropriate relationship between "Student" and "Person" in the context of
object-oriented programming (OOP) is typically described as an "is-a" relationship,
and this relationship is best represented by inheritance.

Inheritance:

Inheritance is a fundamental concept in OOP where a new class (subclass or derived
class) can inherit attributes and behaviors from an existing class (superclass or
base class).
The subclass is a specialized version of the superclass, inheriting its features
and potentially adding or modifying them.
"Student" and "Person" Relationship:

In this scenario, "Student" is a type of "Person." Every student is a person but
with additional characteristics specific to being a student, such as a student ID,
enrolled courses, grades, etc.
Therefore, it makes sense to model this relationship using inheritance, where
"Student" is a subclass of "Person."

'''

