#Write a Python program to read last n lines of a file.

try:
    with open("demo.txt","r") as o:
       lines=o.readlines()

    if lines:
        # Print the last line of the file
        
        print("Last line of the file:")
        print(lines[-1].strip())  # Use strip to remove newline characters
    else:
        
        print("File is empty")
        
except:
    print("file is not read")
    
else:
    print("file  Last line sucessfully....")
