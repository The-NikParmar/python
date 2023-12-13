def Display():
        print("\t\tFruit Market Manager")
        print("\n\t\t1) Add Fruite Stoke")
        print("\t\t2) view Fruite Stoke")
        print("\t\t3) Updated Fruite Stoke")

#==========Add Fruit Stoke=======================
dic={}
def Add_fruit ():

    no_fruit = int(input("How Many want enter Fruits"))

    for i in range(no_fruit):

        Fruit_name = input("\nenter Fruit Name")

        dic[Fruit_name]={}
        quantity=int(input("\nEnter the Fruit Quantity:- "))
        price=int(input("\nEnter The Fruit Price"))


        dic[Fruit_name]["quantity"]=quantity
        dic[Fruit_name]["price"]=price

    with open("fruit.txt","w") as data:
                data.write(str(dic))

#==========view Fruit Stoke========================

def View_fruit_stoke ():
    print("Total Fruit Stoke")
    with open("fruit.txt","r") as data:
          print(data.readline())
          
#========== update Fruit Stoke=====================
def update_fruit_stock():
    print("============ Available Fruit Stock ============")
    
    with open("fruit.txt","r") as data:
                print(data.readline())
                
    Fruit_name = input("\nEnter  Fruit Name ")
    n_quantity = int(input("\nEnter  New Fruit Quantity "))
    n_price = int(input("\nEnter New Fruit Price"))

    dic = {}

    try:
      with open('fruit.txt', 'r') as file:
        content = file.read()
        if content:
            dic = eval(content)
    except FileNotFoundError: 
       pass

    # Update the dictionary with the new information
    dic[Fruit_name] = {"quantity": n_quantity, "price": n_price}
   

    # Write the updated dictionary back to the file
    with open('fruit.txt', 'w') as file:
            file.write(str(dic)
    print(f"\nUpdated dictionary:\n{dic}")
        

while True:
        

    Display()

    choice = int(input("\nEnter your Choice"))
    
    if choice == 1:
        Add_fruit()
        
    elif choice == 2:
        View_fruit_stoke()
        
    elif choice == 3:
        update_fruit_stock()
        
    else:
        print("invalid")
      
     
'''
def update_fruit_stoke():
        
        print("============available Fruit Stoke============")
        with open("fruit.txt","r") as data:
                print(data.readline())
                
        Fruit_name = input("\nEnter New Fruit Name ")
        n_quantity = int(input("\nEnter  New Fruit Quantity "))
        n_price = int(input("\nEnter New Fruit Price"))


'''

        
