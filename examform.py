from tkinter import *
from tkinter import ttk
from tkinter import messagebox


wd1 = Tk()
wd1.title("Login")
wd1.geometry("300x150")
wd1.resizable(0, 0)

l1=Label(wd1,text="User name",font="calibri")
l1.place(x=10,y=20)

e1=Entry(wd1,width=20,relief="solid",border=1,font="calibri")
e1.place(x=100,y=20)

l2=Label(wd1,text="Password",font="calibri")
l2.place(x=10,y=60)

e2=Entry(wd1,show="*",width=20,relief="solid",border=1,font="calibri")
e2.place(x=100,y=60)

def login():

    wd3 = Tk()
    wd3.title("Choose Subject")
    wd3.geometry("300x180")
    wd3.resizable(0, 0)

    l9 = Label(wd3, text="Select Subject:", font="calibri")
    l9.place(x=10, y=20)

    rv1 = IntVar()
    r1 = Radiobutton(wd3, text="Python",font="calibri", variable=rv1, value=1,tristatevalue=0)
    r1.place(x=120, y=20)

    r2 = Radiobutton(wd3, text="Java",font="calibri", variable=rv1, value=2,tristatevalue=0)
    r2.place(x=120, y=50)

    r3 = Radiobutton(wd3, text="C++",font="calibri", variable=rv1, value=3,tristatevalue=0)
    r3.place(x=120, y=80)

    def start():
        pass

    b4 = Button(wd3, text="Start Exam", command=start)
    b4.place(x=120, y=130)

    wd3.mainloop()

b1 = Button(wd1, text="Login", command=login)
b1.place(x=100, y=110)

def register():
    wd2 = Tk()
    wd2.title("Register")
    wd2.geometry("300x250")
    wd2.resizable(0, 0)

    l5 = Label(wd2, text="Name",font="calibri")
    l5.place(x=10, y=20)

    e5 = Entry(wd2, width=20,relief="solid",border=1,font="calibri")
    e5.place(x=100, y=20)

    l6 = Label(wd2, text="Roll no",font="calibri")
    l6.place(x=10, y=60)

    e6 = Entry(wd2, width=20,relief="solid",border=1,font="calibri")
    e6.place(x=100, y=60)

    l7 = Label(wd2, text="Class",font="calibri")
    l7.place(x=10, y=100)

    Class = ['FY', 'SY', 'TY']
    Class.insert(0, "Select your Class")
    cb = ttk.Combobox(wd2, width=18,font="calibri")
    cb['value'] = Class
    cb.place(x=98, y=100)
    cb.current(0)

    l8 = Label(wd2, text="Password",font="calibri")
    l8.place(x=10, y=140)

    e8 = Entry(wd2, show="*", width=20,relief="solid",border=1,font="calibri")
    e8.place(x=100, y=140)

    def submit():
        messagebox.showinfo("NOTE DOWN","Username:          \n Password:          ")

    b3 = Button(wd2, text="Submit", command=submit)
    b3.place(x=135, y=190)

    wd2.mainloop()

b2 = Button(wd1, text="Register", command=register)
b2.place(x=150, y=110)

wd1.mainloop()