import Manager  # Import Manager module with Manager functions
import customer  # Import customer module with customer functions

def role_menu():
    # Display the role selection menu
    print("\n\t\t Welcome to The Fruit Market")
    print("\t\t 1. Manager")
    print("\t\t 2. Customer")

role_menu()
role = int(input("Select your Role: "))

if role == 1:  # Manager role
    while True:
        Manager.Display()  # Display Manager menu

        choice = int(input("Enter your Choice: "))
        if choice == 1:
            Manager.Add_fruit()  # Call Manager function to add fruit

        elif choice == 2:
            Manager.View_fruit_stoke()  # Call Manager function to view fruit stock

        elif choice == 3:
            Manager.update_fruit_stock()  # Call Manager function to update fruit stock

        elif choice == 4:
            exit()  # Exit the program

        else:
            print("Please Select Valid Choice")

elif role == 2:  # Customer role
    while True:
        customer.display()  # Display customer menu

        choice = int(input("Enter your Choice: "))
        if choice == 1:
            customer.view_fruit()  # Call customer function to view available fruits

        elif choice == 2:
            customer.buy_fruit()  # Call customer function to buy fruits

        elif choice == 3:
            exit()  # Exit the program

        else:
            print("Please Select valid Choice")
