#Write a Python program to count the number of lines in a text file.
try:
    # Open the file in read mode
    with open("demo.txt", "r") as file:
        # Read all lines from the file
        lines = file.readlines()

        # Count the number of lines
        num_lines = len(lines)

        # Print the result
        print(f"The file has {num_lines} lines.")

except FileNotFoundError:
    # Handle the case where the file is not found
    print("Error: File not found")
else:
    print("\n file in all line count is sucessfully....")
