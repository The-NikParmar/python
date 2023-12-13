# Step 1: Create a text file and write data to it
file_path = "data.txt"

# Writing data to the file
with open(file_path, "w") as file:
    file.write("key1=value1\n")
    file.write("key2=value2\n")
    file.write("key3=value3\n")

# Step 2: Read the text file and create a Python dictionary
my_dictionary = {}

with open(file_path, "r") as file:
    # Read lines from the file
    lines = file.readlines()

    # Process each line to create a dictionary
    for line in lines:
        # Split each line into key and value
        key, value = line.strip().split("=")

        # Add key-value pair to the dictionary
        my_dictionary[key] = value

# Display the created dictionary
print("Python Dictionary:", my_dictionary)
