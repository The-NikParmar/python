choice=0
while choice !=2:
     print("1. table print ")
     print("2.exit")

     choice=int(input("enter your choice"))
     
     if choice==1:
        no=int(input("enter your no"))
        for i in range (11):
            print(no,"x",i,"=",no*i)
     elif choice==2:
        exit()
     else:
        print("over program")
                
                
                    
                  
