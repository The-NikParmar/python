import random


no1=random.randint(1,100)

print(no1)

while(1,100):
      choice = int(input("enter your No"))

      if choice==no1:
          print("you win")
          break
      elif choice<=no1:
          print(" enter think higher")
      elif choice>=no1:
          print("enter think lesser")
      
      
