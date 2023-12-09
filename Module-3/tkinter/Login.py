from tkinter import *
from tkinter import messagebox as msg
import mysql.connector


win=Tk()
win.title("Login")
win.geometry('925x500+300+200')
win.configure(bg="#fff")
win.resizable(False,False)

img = PhotoImage(file="login.png")
Label(win,image=img,bg='white').place(x=50,y=50)

frame=Frame(win,width=350,height=350,bg="white")
frame.place(x=480,y=70)


heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#==========================database connectivity=========================
def connection():
    return mysql.connector.connect(
        user='root',
        host="localhost",
        password='',
        database="logindata",
        )
#=======================Sign in=========================================
def sign_up():
    if user.get()=="" or code.get()=="":
        msg.showinfo("Insert status","Please enterd Fullfill information!..")
    else:
        conn=connection()
        cursor=conn.cursor()
        query="insert into detail(User,pass)values(%s,%s)"
        args=(user.get(),code.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        user.delete(0,'end')
        code.delete(0,'end')
        Label(win,text="Sign up Sucessfully....",bg="white",fg="#57a1f8",font=('Microsoft YaHei UI Light',15,'bold')).place(x="580",y="420")

#===============================user Username=============================
def on_enter(e):
    user.delete(0,'end')
    
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
        
user = Entry(frame, width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12,'bold'))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)


Frame(frame,width=295,bg='black',height=2).place(x=25,y=107)

#===============================user password==========================
def on_enter(e):
    code.delete(0,'end')
    
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

        
code =  Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12,'bold'))
code.place(x=30,y=160)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,bg='black',height=2).place(x=25,y=185)

#=================================Button================================

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=sign_up    ).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9,'bold'))
label.place(x=75,y=270)

sign_up= Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=236,y=270)

win.mainloop()
