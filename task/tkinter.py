from tkinter import *
#from tkinter import ttk

class FruitStoreApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Fruit Store")

        # Initialize variables
        self.fruits = {"Apple": 1.00, "Banana": 0.75, "Orange": 1.20, "Grapes": 2.50, "Watermelon": 5.00, "Mango": 3.00}
        self.cart = {}

        # Create and configure widgets
        self.create_widgets()

    def create_widgets(self):
        # Label and Listbox for available fruits
        ttk.Label(self.master, text="Available Fruits").grid(row=0, column=0, columnspan=2, pady=10)
        self.fruit_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, height=6)
        for fruit in self.fruits.keys():
            self.fruit_listbox.insert(tk.END, fruit)
        self.fruit_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # Quantity Entry
        ttk.Label(self.master, text="Quantity:").grid(row=2, column=0, padx=10)
        self.quantity_entry = ttk.Entry(self.master)
        self.quantity_entry.grid(row=2, column=1, padx=10)

        # Add to Cart Button
        ttk.Button(self.master, text="Add to Cart", command=self.add_to_cart).grid(row=3, column=0, columnspan=2, pady=10)

        # Cart Display
        ttk.Label(self.master, text="Shopping Cart").grid(row=4, column=0, columnspan=2, pady=10)
        self.cart_text = tk.Text(self.master, height=6, width=30)
        self.cart_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def add_to_cart(self):
        selected_index = self.fruit_listbox.curselection()
        quantity = self.quantity_entry.get()

        if selected_index and quantity.isdigit() and int(quantity) > 0:
            selected_fruit = self.fruit_listbox.get(selected_index)
            price = self.fruits[selected_fruit]
            total_price = price * int(quantity)

            if selected_fruit in self.cart:
                self.cart[selected_fruit] += int(quantity)
            else:
                self.cart[selected_fruit] = int(quantity)

            # Update cart display
            self.update_cart_display()

            # Display a confirmation message
            message = f"Added {quantity} {selected_fruit}(s) to the cart. Total Price: ${total_price:.2f}"
            tk.messagebox.showinfo("Added to Cart", message)
        else:
            tk.messagebox.showwarning("Invalid Input", "Please select a fruit and enter a valid quantity.")

    def update_cart_display(self):
        self.cart_text.config(state=tk.NORMAL)
        self.cart_text.delete(1.0, tk.END)

        total_price = 0.0
        for fruit, quantity in self.cart.items():
            price = self.fruits[fruit]
            total_price += price * quantity
            self.cart_text.insert(tk.END, f"{fruit} x{quantity}: ${price * quantity:.2f}\n")

        self.cart_text.insert(tk.END, f"\nTotal Price: ${total_price:.2f}")
        self.cart_text.config(state=tk.DISABLED)

def main():
    root = Tk()
    app = FruitStoreApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
