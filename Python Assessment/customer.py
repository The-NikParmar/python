def display():
    print("\t\tWelcome to Fruit Market Store")
    print("\n\t\t 1.View Available Fruits")
    print("\n\t\t 2.Buy Fruits")
    print("\n\t\t 3.exit")


def view_fruit():
    print("==================Available Fruits==================")
    with open("fruit.txt","r") as data:
        print(data.readline())

def buy_fruit():
    # Load the existing dictionary from the file
    filename = "fruit.txt"
    dic = {}

    try:
        with open(filename, 'r') as file:
            content = file.read()
        if content:
            dic = eval(content)
    except FileNotFoundError:
        pass

# Display the current available fruits
    print("\nAvailable Fruits:")
    for fruit, details in dic.items():
        print(f"{fruit}: Quantity - {details['quantity']}, Price - {details['price']}")

# Get user input for the fruit to buy
    fruit_to_buy = input("\nEnter the Fruit you want to buy: ")

# Check if the fruit exists in the dictionary
    if fruit_to_buy in dic:
    # Get the quantity to buy
        quantity_to_buy = int(input("\nEnter the quantity you want to buy: "))

    # Check if there is enough quantity available
        if quantity_to_buy <= dic[fruit_to_buy]["quantity"]:
            
        # Calculate the total cost
            total_cost = quantity_to_buy * dic[fruit_to_buy]["price"]

        # Update the dictionary with the new quantity
            dic[fruit_to_buy]["quantity"] -= quantity_to_buy

        # Write the updated dictionary back to the file
            with open(filename, 'w') as file:
                    file.write(str(dic))

            print(f"\nYou have successfully bought {quantity_to_buy} {fruit_to_buy}(s).")
            print(f"Total cost: {total_cost}")
        else:
            print(f"\nSorry, not enough quantity of {fruit_to_buy} available.")
    else:
        print(f"\nSorry, {fruit_to_buy} is not available.")

        print("\nUpdated Fruit Inventory:")
    for fruit, details in dic.items():
        print(f"{fruit}: Quantity - {details['quantity']}, Price - {details['price']}")


