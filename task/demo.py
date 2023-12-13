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

    with open("dic.txt","w") as data:
        data.write(str(dic))

Add_fruit()
