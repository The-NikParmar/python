from tkinter import Tk,Label,Entry,Button

t=Tk()

t.title("Arithmatic Opration")
t.geometry('500x500')
t.resizable(False,False)

# ===================================================================

Heading=Label(t,text="Enter Any Two Numbers",bg="Black",fg="white",font=("Arial 16"))
Heading.place(x=150,y=90)
no1=Label(t, text="Enter Number 1 : ", font=('Arial 14'))
no1.place(x=70,y=129)

inp=Entry(t,)
inp.place(x=229,y=135)

no2=Label(t, text="Enter Number 2 : ", font=('Arial 14'))
no2.place(x=70,y=180)

inp1=Entry(t,)
inp1.place(x=229,y=185)

#button

add=Button(t,text="ADD",command=get_data)
add.place(x=80,y=225)

sub=Button(t,text="Sub")
sub.place(x=160,y=225)

mul=Button(t,text="Mul")
mul.place(x=240,y=225)

div=Button(t,text="Div")
div.place(x=320,y=225)


