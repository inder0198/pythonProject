from tkinter import *
from tkinter import messagebox

def check():
    try:
        a=int(e1.get())
        if a>18:
            messagebox.showinfo("message","you are eligible to vote")
        else:
            messagebox.showerror("message","you are not eligible to vote")
    except ValueError:
        messagebox.showerror("Error","Enter only number")

wind=Tk()
wind.geometry("300x300")

l1=Label(wind,text="enter age").place(x=10,y=10)
e1=Entry(wind,width=15)
e1.place(x=70,y=10)
b1=Button(wind,text="submit",command=check).place(x=50,y=90)

wind.mainloop()