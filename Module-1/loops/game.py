import random

no=random.randint(1,100)
print(no)

status=True
c=1
while(c<=5 and status):
     choice =int(input("enter your no "))
     print("chanse",c)

     c+=1

     if choice==no :
         print("you won")
         break
     elif choice>no:
         print("think lesser")
     elif choice<no:
         print("think higher")


     if c>5:
         con=input("do you want to continue game y/n ?")

         if con=='y':
             c=1
             status=True
         else:
             status=False
