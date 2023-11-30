import os

if os.path.exists("C:\\Users\\dell\\Desktop\\Tops\\git\\python\task\\file management programs\\demo.txt"):
	os.remove("C:\\Users\\dell\\Desktop\\Tops\\git\\python\task\\file management programs\\demo.txt")

else:
	print("File not found")

print("File Delete Sucessfully...")