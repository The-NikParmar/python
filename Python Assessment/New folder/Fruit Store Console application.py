# main.py
from Fruite_Manager import FruiteManager
from customer import Customer

def display_menu(role):
    if role == "1":
        print("\nFruit Market (Manager)")
        print("1. ADD Fruit Stoke")
        print("2. View Fruit Stoke")
        print("3. Update Fruite Stoke")
       
    elif role == "2":
        print("\nFruit Market (Customer)")
        print("1. View Available Fruits")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. View Transactions")
        print("6. Exit")

def main():
    print(" WELCOME TO FRUITE MARKER")
    print("1) Manager")
    print("2) customer")
    role = input("Select your Role :  ")

    if role not in ["1", "2"]:
        print("Invalid role. Exiting.")
        return

    fruit_manager = FruiteManager()

    if role == "1":
        while True:
            display_menu(role)
            choice = input("Enter your choice: ")

            if choice == "2":
                fruit_manager.view_stock()
            elif choice == "1":
                fruit = input("Enter the fruit to add: ")
                price = float(input("Enter the price per unit: "))
                quantity = int(input("Enter the quantity to add: "))
                fruit_manager.add_to_stock(fruit, price, quantity)
            elif choice == "3":
                fruit = input("Enter the fruit to update: ")
                new_price = float(input("Enter the new price per unit: "))
                fruit_manager.update_stock(fruit, new_price)
            else:
                print("Invalid choice. Please enter a valid option.")

    elif role == "2":
        customer = Customer(fruit_manager)

        while True:
            display_menu(role)
            choice = input("Enter your choice: ")

            if choice == "1":
                customer.view_available_fruits()
            elif choice == "2":
                fruit = input("Enter the fruit to add to the cart: ")
                quantity = int(input("Enter the quantity to add to the cart: "))
                customer.add_to_cart(fruit, quantity)
            elif choice == "3":
                customer.view_cart()
            elif choice == "4":
                customer.checkout()
            elif choice == "5":
                customer.view_transactions()
            elif choice == "6":
                print("Exiting the Fruit Market (Customer).")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
