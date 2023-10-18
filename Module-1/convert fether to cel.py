print("What do you want to convert")
print("1 for Fehrenhit to Celcius")
print("2 for Celcius to Fehrenhit")
choice=int(input("Enter your choice = "))
if(choice==1):
     fehrenhit=float(input("Enter Fehrenhit = "))
     celcius=(fehrenhit-32)*5/9
     print("After converting Fehrenhit in to Celcius = ",celcius)
elif(choice==2):
     celcius=float(input("Enter Celcius = "))
     fehrenhit=(celcius*9/5)+32
     print("After converting Celcius in to Fehrenhit   = ",fehrenhit)
else:
    print("Enter valid choice")
