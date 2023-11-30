#Write a Python program to read a file line by line and store it into a list

try:
    # open the file "demo.txt" in read mode
    with open("demo.txt", "r") as o1:
        # Read all lines from the file and store them in the list
        lines = o1.readlines()
        
        # Print the content of the file (all lines)
        print(lines)

except FileNotFoundError:
    # Handle the case where the file is not found
    print("File not found")

else:
    #nthis block executes if the 'try' block is successful
    print("File read successfully.")
