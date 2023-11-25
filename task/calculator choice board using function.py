def choice_board():
    
    print("=============choice board===============")
    status = True

    while status:
    

        print("1.addition")
        print("2.subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Modullo")

        no = int(input("\nEnter Your Choice"))
        
        if no==1:

            no1=int(input("\nEnter Your Number 1 :- "))
            no2=int(input("Enter Your Number 2 :- "))

            print("\nAddition of Two Numbers :- ",no1+no2)
            
        elif no==2:

            no1=int(input("\nEnter Your Number 1 :- "))
            no2=int(input("Enter Your Number 2 :- "))
            
            print("\nSubstraction of Two Numbers :- ",no1-no2)

        elif no==3:

            no1=int(input("\nEnter Your Number 1 :- "))
            no2=int(input("Enter Your Number 2 :- "))

            print("\nMultipilication of Two Numbers :- ",no1*no2)

        elif no==4:

            no1=int(input("\nEnter Your Number 1 :- "))
            no2=int(input("Enter Your Number 2 :- "))

            print("\nDivision of Two Numbers :- ",no1/no2)

        elif no==5:

            no1=int(input("Enter Your Number 1 :-"))
            no2=int(input("Enter Your Number 2 :- "))

            print("\nModulo of Two Numbers :- ",no1%no2)
        else:
            exit()
            
        choice=input("\ndo you want to continue ? :['y/n']:")

        if choice=='y':
            status = True
        else:
            status = False

choice_board()

          
