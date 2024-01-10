import os 
import datetime

#if os.path.exists("Vaccination"):
current_datetime = datetime.datetime.now()   

formatted_date = current_datetime.strftime("%d-%m-%Y")
formatted_time = current_datetime.strftime("%H-%M-%S")

filename = f"{formatted_date}__{formatted_time}.txt"

name = input("Enter your Name:- ")
age = int(input("Enter your Age:- "))
mo = int(input("Enter your Contect Number :- "))
vacine = input("Enter your vacine Name:- ")
doze = int(input("Enter your vacine doze:- "))

with open(filename,'w') as data:
        data.write("\n\t\tVaccination Report")
        data.write("\n==============================================")
        data.write(f"\nDate:- {formatted_date} Time:-{formatted_time}\n")
        data.write(f"\nName            :- {name}")
        data.write(f"\nAge             :- {str(age)}")
        data.write(f"\nContect Number  :- {str(mo)}")
        data.write(f"\nvacine Name     :- {vacine}")
        data.write(f"\nvacine Doze     :- {str(doze)}")
        
print(f"File '{filename}' created with the vaccinatona data.")


        


    

    
    

