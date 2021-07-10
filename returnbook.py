from tkinter import *

wd9 = Tk()
wd9.title("Return Book")
wd9.geometry("300x140")
wd9.resizable(0, 0)

l1=Label(wd9,text="Book ID",font=("calibri"))
l1.place(x=30,y=30)

e1=Entry(wd9,width=20,relief="solid",border=1,font=("calibri"))
e1.place(x=105,y=30)

def returnbook():
    pass

b1 = Button(wd9, text="Return",font=("calibri"), command=returnbook)
b1.place(x=90, y=80)

def quit():
    pass

b2 = Button(wd9, text="Quit",font=("calibri"), command=quit)
b2.place(x=160, y=80)

wd9.mainloop()