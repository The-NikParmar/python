# Write a Python program to read first n lines of a file.

# Open the file named "demo.txt" in read mode ("r")
with open("demo.txt", "r") as o:
    # Read the first line of the file and print it
    print(o.readline())


