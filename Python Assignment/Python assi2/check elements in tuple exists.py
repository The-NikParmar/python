#  Write a Python program to check whether an element exists within a tuple. 


my_tuple = (111, 22, 83,'nikhil','good',34,76,24)
element = 'nikhil'

for i in my_tuple:
  if i == element:
    print(f"{element} Element exists in tuple")
    break
else:
  print("Element does not exist in tuple")
