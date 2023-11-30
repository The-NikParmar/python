#Write a Python program to append text to a file and display the text.

try:
    with open("demo.txt","a") as f1:
        f1.write(" Demo file in data append Sucefully")
        with open("demo.txt","r") as f2:
            print(f2.read())
except:
    print("data is not append in file")
else:
    print("data apeend sucessfully...")
