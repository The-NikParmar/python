#Write a python program to find the longest words.
try:
    # Open the file "demo.txt" in read mode
    with open("demo.txt", "r") as f:
        # Read the entire content of the file and split it into words
        words = f.read().split()

        # Assume the first word is the longest
        longest_word = words[0]

        # Iterate through the words to find the longest one
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

        # Print the longest word
        print(f"The longest word is: {longest_word}")

except FileNotFoundError:
    # Handle the case where the file is not found
    print("Error: File not found")

else:
    #this block executes if the 'try' block is successful
    print("Longest word found successfully.")
