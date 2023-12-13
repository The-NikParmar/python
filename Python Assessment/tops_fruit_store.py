import Manager
import customer


def role_menu():
    print("\n\t\t Welcome to The Fruit Market")
    print("\t\t 1. Manager")
    print("\t\t 2. Customer")
    
role_menu()
role=int(input("Select your Role:- "))


if role==1:
    while True:
        Manager.Display()

        choice = int(input("Enter your Choice"))
        if choice==1:
            Manager.Add_fruit()

        elif choice==2:
            Manager.View_fruit_stoke()
        
        elif choice==3:
            Manager.update_fruit_stock()

        elif choice==4:
            exit()
        else:
            print("Please Select Valid Choice")

            
elif role==2:

    while True:
        customer.display()
        choice = int(input("Enter your Choice"))

        if choice==1:
            customer.view_fruit()
            
        elif choice==2:
            customer.buy_fruit()

        elif choice==3:
            exit()

        else:
            print("Please Select valid Choice")


