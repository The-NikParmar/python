f = open("myfile.txt","a")


for i in range(1,6):
    name = input("enter your name:- ")
    f.write("\n"+name)

f.close()