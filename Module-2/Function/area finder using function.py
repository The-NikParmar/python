def area_finder():
    print("================Area Finder=================")
    
    print("1.circle")
    print("2.Triangle")
    print("3.Rectangle")
    #print("4.exit")
    
    choice=int(input("\nEnter Your Choice"))
    
    
    if choice==1:
        radius=int(input("enter your radius"))

        area=radius*3.14

        print("area of circle ",area)
        
    elif choice==2:
        
        height=int(input("enter the height = "))
        base=int(input("enter the base = "))
        
        area=0.5*height*base
        
        print("area of triangle = ",area)
        
    elif choice==3:

        length=int(input("enter the length = "))
        breath=int(input("enter the breath = "))
        
        area=length*breath
        
        print("area of rectangle = ",area)

area_finder()
        


        

    
