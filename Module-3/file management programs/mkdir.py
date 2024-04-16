import os 

if os.path.exists("Myfolder"):
    print("Alredy created")
    #os.rmdir("Myfolder") for delete directory

else:
    os.mkdir("myfolder")
    print("creat")