'''
1.What is List? How will you reverse a list?

    Python comes with a number of methods and functions that allow you to reverse a list,
    either directly or by iterating over the list object. You’ll learn how to reverse a Python
    list by using the reversed() function, the .reverse() met-hod, list indexing, for loops,
    list comprehensions, and the slice method.'''

# 2. How will you remove last object from a list?
'''
using remove  inbulit function and remove last element from list
'''
#  Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?


li=[2,33,222,14,25]

li.remove(25)
print(li)

# 3 Differentiate between append () and extend () methods?
'''
 append() when we want to add a single item to the end of a list and extend()
 when we want to merge our list with another

'''

#example of append method

my_list = []

my_list.append(1)

print("append method ",my_list)

# example of extend method

my_list = [5,6,7]

my_list.extend([1, 2, 3])

print("extend method",my_list)

# 5 How will you compare two lists?

'''

Python: Use the list.sort() method to sort the lists, and then use the == operator to compare
them. The == operator compares the lists item by item, and returns "Equal" if all elements are
the same in the same order.

Excel: Use the Equal Sign Operator, the Row Difference Technique, the IF Condition,
or Power Query.

Graph: Use a Dual Axis Line Chart to compare two sets of data.

'''


# What is tuple?.

'''

A tuple is a collection of Python objects that is ordered and immutable.

This means that the order of elements in a tuple cannot be changed,
and elements cannot be added,removed, or replaced.

Tuples are created using parentheses and elements are separated by commas.
'''

# Difference between list and tuple.

#   Feature	    List	                            Tuple
'''
    Mutability      Mutable           `                     Immutable

    Creation        Created using square brackets ([])      Created using parentheses (())

    Modification   Elements can be add,removed,or replaced  Elements cannot be added, removed, or replaced

'''


