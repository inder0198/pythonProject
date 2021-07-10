from tkinter import *
from tkinter import messagebox
import numpy as np

def generate():
    try:
        a = int(FirstInput.get())
    except ValueError:
        messagebox.showerror("Error","Enter only number")
    try:
        b = int(SecondInput.get())
    except ValueError:
        messagebox.showerror("Error","Enter only number")
    try:
        c = int(Size1Input.get())
    except ValueError:
        messagebox.showerror("Error","Enter only number for Rows")
    try:
        d = int(Size2Input.get())
    except ValueError:
        messagebox.showerror("Error","Enter only number for Columns")
    # a = int(FirstInput.get())
    # b = int(SecondInput.get())
    # c = int(Size1Input.get())
    # d = int(Size2Input.get())
    global mat
    mat = np.random.randint(a , b+1, size=(c, d))
    lb1.config(text=mat)

wd = Tk()
wd. state("zoomed")
wd.title("Matrix Generator")
wd.geometry("1366x720")

# bg=PhotoImage(file="bg2.png")
# l2=Label(wd,image=bg)
# l2.place(x=0,y=0)

Label(wd,text='Matrix & Its Transpose',font=('calibri',30,'bold'),fg='blue').place(x=483,y=30)

Label(wd,text="Enter 1st Positive Number :",font=("calibri",15,"bold")).place(x=100,y=190)
FirstInput= Entry(wd,font=("calibri",15,"bold"),border=1,relief="solid")
FirstInput.place(x=350,y=190)

Label(wd,text="Enter 2nd Positive Number :",font=("calibri",15,'bold')).place(x=680,y=190)
SecondInput= Entry(wd,font=("calibri",15),border=1,relief="solid")
SecondInput.place(x=930,y=190)

Label(wd,text="Enter no of Rows:",font=("calibri",15,"bold")).place(x=100,y=130)
Size1Input= Entry(wd,font=("calibri",15,"bold"),border=1,relief="solid")
Size1Input.place(x=350,y=130)

Label(wd,text="Enter no of Columns:",font=("calibri",15,'bold')).place(x=680,y=130)
Size2Input= Entry(wd,font=("calibri",15),border=1,relief="solid")
Size2Input.place(x=930,y=130)

Button(wd,text='Generate',width=10, font = ("Arial",15),command = generate,border=1,relief="solid").place(x=520,y=260)

lb1 = Label(wd,text="Press generate to get a random Matrix",font = ("Arial",15))
lb1.place(x=150,y=390)

def transpose():
    try:
        transpose = np.transpose(mat)
        lb2.config(text=transpose)
    except NameError:
        messagebox.showerror("Error","Generate a matrix first")

Button(wd,text='Transpose',width=10,font = ("Arial",15), command=transpose,border=1,relief="solid").place(x=660,y=260)

lb2 = Label(wd,text='Press transpose to get transpose of the Matrix',font=("Arial",15))
lb2.place(x=750,y=390)

Label(wd,text='Matrix',font=("Arial",25)).place(x=150,y=340)
Label(wd,text='Transpose',font=("Arial",25)).place(x=750,y=340)

wd.mainloop()




# elif (rv.get() == 3):
# string = Input.get()
# words = string.split(" ")
# newWords = [word[::-1] for word in words]
# newSentence = " ".join(sorted(newWords))
# lb1.config(text=newSentence)


# from string import ascii_letters
# elif (rv.get() == 5):
# string = Input.get()
# fifth = ""
# for c in string:
#     if c in ascii_letters:
#         fifth = fifth + ascii_letters[(ascii_letters.index(c) + 2) % len(ascii_letters)] + " "
#     lb1.config(text=fifth)