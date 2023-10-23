#Write a Python program to find the second smallest number in a list. 

li=[12,432,564,23,56,1,2,456,43,12,464,23,21,132,423,53]

smallest = min(li)
li.remove(smallest)
for num in li:
  if num < min(li):
    smallest = num
print(smallest)

