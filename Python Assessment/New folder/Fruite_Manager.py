class FruitManager:
    
    def __init__(self):
        # Initialize the fruit stock with some default values
        self.fruit_stock = {'Apple': {'price': 70, 'quantity': 20},
                            'Banana': {'price': 30, 'quantity': 15},
                            'Orange': {'price': 50, 'quantity': 25},
                            'Grapes': {'price': 20, 'quantity': 10}}
        
    # =======Add_Stock========================
        
    def add_to_stock(self, fruit, price, quantity):
        print("\nAdd Fruit Stock:")
        if fruit not in self.fruit_stock:
            # If the fruit is not in stock, add it with the specified price and quantity
            self.fruit_stock[fruit] = {'price': price, 'quantity': quantity}
            print(f"{fruit} added to the fruit stock.")
        else:
            # If the fruit is already in stock, display a message
            print(f"{fruit} is already available in the fruit stock.")
            
    # =======View_Stock========================
            
    def view_stock(self):
        print("\nFruit Stock:")
        for fruit, details in self.fruit_stock.items():
            # Display the quantity and price of each fruit in stock
            print(f"{fruit}: {details['quantity']} in stock - ${details['price']} per unit")
            
    # =======Update_Stock===================
            
    def update_stock(self, fruit, new_quantity):
        if fruit in self.fruit_stock:
            # If the fruit is in stock, update its quantity
            self.fruit_stock[fruit]['quantity'] = new_quantity
            print(f"Quantity of {fruit} updated to {new_quantity}.")
        else:
            # If the fruit is not in stock, display a message
            print(f"{fruit} is not found in the fruit stock. Cannot update quantity.")
            
    # =======View_Available_Fruits================
            
    def view_available_fruits(self):
        print("\nAvailable Fruits:")
        for fruit, details in self.fruit_stock.items():
            # Display the available fruits along with their quantity and price
            print(f"{fruit}: {details['quantity']} in stock - ${details['price']} per unit")
     
