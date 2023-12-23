class OrderSystem:
    def __init__(self):
        self.total_net_amount = 0
        self.total_pizza_sales = 0          
        self.total_momos_sales =0
        self.total_soft_drink =0
        self.total_French_frise=0
        self.total_burger =0

    def add (self,p,m):
        if p>=4 and m>=4:
            self.total_burger += 2

    def place_order(self, item, quantity):            
        if item == 1:  # small Pizza
            cost = 220 * quantity
            self.total_pizza_sales += quantity
            
            if quantity>=4:
                self.total_soft_drink += 1
            print("The Total Pizza Amount is",cost)
        elif item == 2:
            cost = 100 * quantity
            self.total_momos_sales += quantity

            if quantity>=4:
                self.total_French_frise += 1
            print("The Total Momos Amount is",cost)

        else:
            print("Invalid item")
            return

        self.total_net_amount += cost
        print(f"\t\t=============================Total Net Amount:{self.total_net_amount}===============================")

    def display_statistics(self):
        print("Payment received from pizza:", 220 *self.total_pizza_sales)
        print("Payment received from Momos:", 100 *self.total_momos_sales)
        print("Total  Pizza Sales:        ",  self.total_pizza_sales)
        print("Total  Momos Sales:        ",  self.total_momos_sales)
        print("Total  1.5lit cold Drinks: ",self.total_soft_drink)
        print("Total  French Frise:       ",self.total_French_frise)
        print("Total Burger:              ",self.total_burger)
        print("Total Net Amount:          ", self.total_net_amount)

    def food_menu(self):
            
            print("======================================Welcome to the Pizza Point======================================")
            print("\n\t\t1.Order Menu")
            print("\t\t2.Exit")

            choice = int(input("\n Enter your Choice:- "))
            print("================================================Food Menu====================================================")
            if choice==1:
                print("\n 1. Pizza = 220rs")
                print("\n ***Buy 4 or more pizza and get 1.5lt of soft drink free***")
                print("\n 2. Momos = 100rs ")
                print("\n ***Buy 4 or more  Momos and get 1 French-Frise free.***")
                print("\n ***Buy 4 or more pizzas and Momos and get 2 Burger free.")
            elif choice==2:
                exit()

o1=OrderSystem()
status =True

while status:
    o1.food_menu()
    item=int(input("\nSelect your Order"))
    if item==1:
        p_qn=int(input("Enter your Pizza Quantity"))
        if p_qn>=4:
            print("*** Congratulations !! 1.5lt softdrink free *** ")
            o1.place_order(item,p_qn)
        else:
            o1.place_order(item,p_qn)
  
    
    print("\n Enter Momos Order")
    item=int(input("\nSelect your Momos"))
    if item==2:
        m_qn=int(input("Enter your Momos quantity"))
        if m_qn>=4:
            print("*** Congratulations !! 1 French-Frise free. *** ")
            if m_qn>=4 and p_qn>=4:
                print("*** Congratulations !! 2 Burger  free *** ")
            o1.add(p_qn,m_qn)
            o1.place_order(item,m_qn)
        else:
            o1.place_order(item,m_qn)
    

    choice=input("do you want to continue ? :['y/n']:")

    if choice=='y':
        status = True
    else:
        status = False
        o1.display_statistics()


    




















'''
item=int(input("\n Select your pizza"))

if item==1:
    qn=int(input("enter your quantity"))
    if qn>4:
        print("*** Congratulations !! 1.5lt softdrink free *** ")
        o1.place_order(item,qn)
    else:
        o1.place_order(item,qn)
    

elif item==2:
    qn=int(input("enter your quantity"))
    if qn>4:
        print("*** Congratulations !! 1.5lt softdrink free *** ")
        o1.place_order(item,qn)
    else:
        o1.place_order(item,qn)

print("enter Momos order")
item=int(input("\n Select your Momos"))
if item==3:
    qn=int(input("enter your momos quantity"))
    if qn>=4:
        print("*** Congratulations !! French-Frise free *** ")
        o1.place_order(item,qn)
    else:
        o1.place_order(item,qn)


o1.display_statistics()

    '''
