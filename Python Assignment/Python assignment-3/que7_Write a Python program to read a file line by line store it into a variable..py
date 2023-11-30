#Write a Python program to read a file line by line store it into a variable.

try:
    with open("demo.txt","r") as f:

        variable=f.read()

        print("the file stored in a variable")
        print("\n",variable)

except:
    print("file is not read")
else:
    print("\nfile is read line by line and store in variable sucessfullly..")
