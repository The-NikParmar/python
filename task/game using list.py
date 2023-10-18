import random
li=[]
us=[]
cm=[]
n=0

# ask to User random  12 numbers
for i in range(1,13):
    num=int(input(f"Enter your Number {n+1} : "))

    li.append(num)
    n+=1
print("The Total Number of List",li)

# insert in two elemts list
n1=1
for i in li:
    if n1%2==0:
        us.append(i)
    else:
        cm.append(i)
    n1+=1

print("\nThe Elements of User",us)
print("\nThe Elements of Computer",cm)
  
      
# start game
print("\n|||||||||||||||||||||||>>> START GAMNE <<<|||||||||||||||||||||||")
c_count=0
u_count=0
c=1
u=1
for i in range(1,13):
    
    rn=random.choice(li)

    if rn in us:
        us.remove(rn)
        u_count +=1
        print(f"\n New user list {u}",us)
        print(f"New computer list {c}",cm)
        print(f"\nThe Userscore:- {u_count}")
    elif rn in cm:
        cm.remove(rn)
        c_count +=1
        print(f"\n New user list {u}",us)
        print(f"New computer list {c}",cm)
        print(f"\nThe Computer-Score:- {c_count}")
    li.remove(rn)

    c+=1
    u+=1
    if c_count==6:
        print("\nComputer is win")
        break
    elif u_count==6:
        print("\nUser is win")
        break
