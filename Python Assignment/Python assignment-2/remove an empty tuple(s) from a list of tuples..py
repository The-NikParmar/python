#Write a Python program to remove an empty tuple(s) from a list of tuples.

li=[(),('s','n'),('Nikhil'),()]

for i in li:
    if i == ():
        li.remove(i)
print(li)
