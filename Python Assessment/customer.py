# customer.py
import datetime

class Customer:
    def __init__(self, fruit_manager):
        self.cart = {}
        self.fruit_manager = fruit_manager
        self.transactions = []

    def view_available_fruits(self):
        self.fruit_manager.view_available_fruits()

    def add_to_cart(self, fruit, quantity):
        if fruit in self.fruit_manager.fruit_stock:
            if fruit in self.cart:
                self.cart[fruit] += quantity
            else:
                self.cart[fruit] = quantity
            print(f"{quantity} {fruit}(s) added to the cart.")
        else:
            print(f"{fruit} is not available in the fruit market.")

    def view_cart(self):
        print("\nYour Cart:")
        for fruit, quantity in self.cart.items():
            print(f"{fruit}: {quantity} in cart")

    def checkout(self):
        total_price = 0.0
        print("\nCheckout:")
        for fruit, quantity in self.cart.items():
            if fruit in self.fruit_manager.fruit_stock:
                price_per_unit = self.fruit_manager.fruit_stock[fruit]['price']
                total_price += price_per_unit * quantity
                print(f"{fruit}: {quantity} x ${price_per_unit} = ${price_per_unit * quantity}")
            else:
                print(f"{fruit} is not available in the fruit stock.")

        timestamp = str(datetime.datetime.now())
        transaction = {'timestamp': timestamp, 'items': self.cart.copy(), 'total_price': total_price}
        self.transactions.append(transaction)

        print(f"Total Price: ${total_price}")
        print("Thank you for shopping!")

        # Clear the cart after checkout
        self.cart = {}

    def view_transactions(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(f"Timestamp: {transaction['timestamp']}")
            for fruit, quantity in transaction['items'].items():
                print(f"{fruit}: {quantity}")
            print(f"Total Price: ${transaction['total_price']}")
            print("-" * 20)
