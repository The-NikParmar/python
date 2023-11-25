def tops():

    status = True
    global total
    total=0
    while status:

        print("===============Welcome to Tops Restaurant==============")

        print("SrNo.      item        Price")
        print("1          Pizza       90/-")
        print("2          Burger      89/-")
        print("3          Pani-puri   100/-")
        print("4          Dosa        80/-")

        no=int(input("Enter your Choice"))
        if no==1:
            print("You have Selected Pizza.")

            qun=int(input("\nEnter The Quntity :- "))

            a1 =qun*90
            total=total+a1
            print("Total Price :- ",a1)

        elif no==2:
            print("you have Selected Burger")

            bu=int(input("\nEnter The Quntity"))

            a2=bu*89
            print("Total Price :-",a2)
            
        elif no==3:
            print("you have Selected Pani-puri")

            pa=int(input("\nEnter The Quntity"))

            a3=pa*100
            print("Total Price :-",a3)

        elif no==4:
            print("you have Selected Dosa")

            do=int(input("\nEnter The Quntity"))

            a4=do*80
            print("Total Price :-",a4)
        else:
            print("Please select valid choice")

        choice=input("\ndo you want to continue ? :['y/n']:")

        total=0
        global g
        
        if choice=='y':
            status = True
        else:
            status = False

            print("total is",total)
   
tops()
    
