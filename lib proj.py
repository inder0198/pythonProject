from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as m

conn = m.connect(user="root", password="root", host="localhost", database="library")
cur = conn.cursor()


def login():
    pass

wd1 = Tk()
wd1.title("Login")
wd1.geometry("300x150")
wd1.resizable(0, 0)

l1=Label(wd1,text="User name:")
l1.place(x=10,y=20)

e1=Entry(wd1,width=30)
e1.place(x=85,y=18)

l2=Label(wd1,text="Password:")
l2.place(x=10,y=60)

e2=Entry(wd1,show="*",width=30)
e2.place(x=85,y=58)

b1=Button(wd1,text="Login",command=login)
b1.place(x=130,y=110)

wd1.mainloop()