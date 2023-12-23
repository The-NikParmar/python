def Display():
    # Display the main menu for the Fruit Market Manager
    print("\n\t\tFruit Market Manager")
    print("\n\t\t1) Add Fruite Stoke")
    print("\t\t2) View Fruite Stoke")
    print("\t\t3) Update Fruite Stoke")
    print("\t\t4) Exit")

# ==========Add Fruit Stoke=======================
dic = {}  # Initialize an empty dictionary to store fruit information

def Add_fruit():
    # Add fruits to the dictionary with quantity and price
    no_fruit = int(input("How many fruits do you want to enter?"))

    for i in range(no_fruit):
        Fruit_name = input("\nEnter Fruit Name: ")
        dic[Fruit_name] = {}
        quantity = int(input("Enter the Fruit Quantity: "))
        price = int(input("Enter The Fruit Price: "))

        dic[Fruit_name]["quantity"] = quantity
        dic[Fruit_name]["price"] = price

    # Write the dictionary to the "fruit.txt" file
    with open("fruit.txt", "w") as data:
        data.write(str(dic))

# ==========View Fruit Stoke========================
def View_fruit_stoke():
    # View the total fruit stock by reading from the "fruit.txt" file
    print("Total Fruit Stoke:")
    with open("fruit.txt", "r") as data:
        print(data.readline())

# ==========Update Fruit Stoke=====================
def update_fruit_stock():
    print("============ Available Fruit Stock ============")

    # Display the current available fruit stock by reading from the "fruit.txt" file
    with open("fruit.txt", "r") as data:
        print(data.readline())

    # Get user input for the fruit to update
    fruit_name = input("\nEnter Fruit Name to Update: ")

    # Get the current quantity and price from the file
    try:
        with open('fruit.txt', 'r') as file:
            content = file.read()
            if content:
                stock_data = eval(content)
                current_quantity = stock_data.get(fruit_name, {}).get("quantity", 0)
                current_price = stock_data.get(fruit_name, {}).get("price", 0)
    except FileNotFoundError:
        current_quantity = 0
        current_price = 0

    # Get user input for the change in quantity and price
    quantity_change = int(input(f"\nEnter Change in Quantity for {fruit_name}: "))
    price_change = int(input(f"\nEnter Change in Price for {fruit_name}: "))

    # Calculate the new quantity and price
    new_quantity = current_quantity + quantity_change
    new_price =  price_change

    # Update the dictionary with the new data
    stock_data[fruit_name] = {"quantity": new_quantity, "price": new_price}

    # Write the updated dictionary back to the file
    with open('fruit.txt', 'w') as file:
        file.write(str(stock_data))

    print(f"\nUpdated dictionary:\n{stock_data}")












