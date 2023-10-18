no = int(input("enter your no "))

ch='A'

for i in range (no):
    for j in range(i):
        print(ch,end=" ")
        ch+=1;
    print()
    
