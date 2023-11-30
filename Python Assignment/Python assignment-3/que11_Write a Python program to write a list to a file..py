#Write a Python program to write a list to a file.

# Example list
my_list = ["apple", "banana", "orange", "grape"]

try:
    # Open the file in write mode
    with open("list.txt", "w") as file:
        # Write each item in the list to the file
        for i in my_list:
            file.write(f"{i}\n")

    print("List successfully written to file.")

except:
    print("list data Not write in file")

else:
    print("lis all data write in file")
