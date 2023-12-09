from tkinter import *
from tkinter import messagebox
import mysql.connector

win=Tk()

win.title("Student Registartion From")
win.geometry("500x500")
win.resizable(False,False)

#===========================Data base connectivity=====================================
def connection():
    return mysql.connector.connect(   
        user = 'root',
        host = "localhost",
        password = '',
        database = "mydata")


#=============================registration=============================================
def register():
    name = name_info.get()
    age = age_info.get()
    email = email_info.get()
    mob = mo_info.get()

    if name=="" or age=="" or email=="" or mob=="":
        messagebox.showerror("Error","please enter valid information")
    else:

        con=connection()
        cursor = con.cursor() 
        query = "insert into student(Name,Age,Email,mobile) values(%s,%s,%s,%s)"
        args=(name_entry.get(),Age_entry.get(),Email_entry.get(),Mo_entry.get())
        cursor.execute(query,args)
        con.commit()
        con.close()
        name_entry.delete(0,'end')
        Age_entry.delete(0,'end')
        Email_entry.delete(0,'end')
        Mo_entry.delete(0,'end')
        Label(win,text="Registraion Sucessfully",bg="Green",fg="white",font="18").place(x="150",y="420")

#================Label-Heading================================

Label(win,text="Student Registration From",font=("Airal 14 bold"),fg="white",bg="black").pack(fill="both")

name=Label(win,text="Name:- ",font="20").place(x=50,y=100)

age=Label(win,text="Age:- ",font="20").place(x=50,y=150)

email=Label(win,text="Email:- ",font="20").place(x=50,y=200)

mobi=Label(win,text="Mobile No:- ",font="20").place(x=50,y=250)

#===============Entry-user input==============================

name_info = StringVar()
age_info = StringVar()
email_info = StringVar()
mo_info = StringVar()

name_entry = Entry(win,font="10",bd="5" ,textvariable=name_info)
name_entry.place(x=190,y=100)

Age_entry = Entry(win,font="10",bd="5" ,textvariable=age_info)
Age_entry.place(x=190,y=150)

Email_entry = Entry(win,font="10",bd="5", textvariable=email_info)
Email_entry.place(x=190,y=200)

Mo_entry = Entry(win,font="10",bd="5", textvariable=mo_info)
Mo_entry.place(x=190,y=250)

#==============Button Registration=============================

Button(win,text="Registration",font=" Arial 16 bold",bd="5" ,command=register).place(x="150",y="320")

mainloop()
