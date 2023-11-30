# Write a Python program to copy the contents of a file to another file.
try:
    # Open the source file "A.txt" for reading
    with open("A.txt", "r") as f1:
        # Open the destination file "B.txt" for writing
        with open("B.txt", "w") as f2:
            # Iterate through each line in the source file and write it to the destination file
            for line in f1:
                f2.write(line)

except FileNotFoundError:
    # Handle the case where the source file is not found
    print("Error: Source file 'A.txt' not found.")
else:
    # Close the source file
    f1.close()
    print("Source file closed.")


