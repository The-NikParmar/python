from tkinter import *
 
def add_numbers():
    res=int(e1.get())+int(e2.get())
    label_text.set(res)
 
window = Tk()
label_text=StringVar();
Label(window, text="Enter First Number:").grid(row=0, sticky=W)
Label(window, text="Enter Second Number:").grid(row=1, sticky=W)
Label(window, text="Result of Addition:").grid(row=3, sticky=W)
result=Label(window, text="", textvariable=label_text).grid(row=3,column=1, sticky=W)
 
e1 = Entry(window)
e2 = Entry(window)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
 
b = Button(window, text="Calculate", command=add_numbers)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
 
mainloop()
 
