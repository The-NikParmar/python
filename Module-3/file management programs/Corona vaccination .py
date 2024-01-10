import os 
import datetime

if os.path.exists("Vaccination"):
    
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"data_{current_date}.txt"

    name = input("Enter your Name:- ")
    age = int(input("Enter your Age:- "))
    vacine = input("Enter your vacine Name:- ")
    doze = int(input("Enter your vacine doze:- "))

    with open(filename,'w') as data:
        data.write(name)
        data.write(str(age))
        data.write(vacine)
        data.write(str(doze))
        
    print(f"File '{filename}' created with the sample data.")


        


    

    
    

