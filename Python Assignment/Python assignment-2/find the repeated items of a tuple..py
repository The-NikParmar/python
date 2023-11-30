# Write a Python program to find the repeated items of a tuple.

tup = (111, 222, 39, 222, 34, 39, 35)
repeated_items = []
for item in tup:
  count = 0
  for i in tup:
    if item == i:
      count += 1
  if count > 1:
    if item not in repeated_items:
      repeated_items.append(item)

print("Repeated items:", repeated_items)
