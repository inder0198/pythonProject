import tkinter as tk
from tkinter import *
from tkinter import messagebox

w=Tk()
w.title("Python")
w.geometry("800x800")

l=Label(w,text="Python MCQ(Multiple Choice Questions)",font=("calibri",25))
l.place(x=50,y=30)
ll=Label(w,text="Timer",font=("calibri"))
ll.place(x=700,y=10)


mv1 = IntVar()
l1=Label(w,text="1) What is the maximum possible length of an identifier ? ",font="calibri")
l1.place(x=50,y=130)
m11 = Radiobutton(w, text="  16", font='calibri', variable=mv1, value=1)
m11.place(x=75, y=170)
m12 = Radiobutton(w, text="  32", font='calibri', variable=mv1, value=2)
m12.place(x=280, y=170)
m13 = Radiobutton(w, text="  64", font='calibri', variable=mv1, value=3)
m13.place(x=75, y=210)
m14 = Radiobutton(w, text="  None of the Above", font='calibri', variable=mv1, value=4)
m14.place(x=280, y=210)


mv2 = IntVar()
l2=Label(w,text="2) Who developed the Python language? ",font="calibri")
l2.place(x=50,y=270)
m21 = Radiobutton(w, text="  Zim Den", font='calibri', variable=mv2, value=1)
m21.place(x=75, y=310)
m22 = Radiobutton(w, text="  Guido Van Rossum", font='calibri', variable=mv2, value=2)
m22.place(x=280, y=310)
m23 = Radiobutton(w, text="  Harsal Wankhede", font='calibri', variable=mv2, value=3)
m23.place(x=75, y=350)
m24 = Radiobutton(w, text="  Wick Van Rossum", font='calibri', variable=mv2, value=4)
m24.place(x=280, y=350)


mv3 = IntVar()
l31=Label(w,text="3) In which year was the Python language developed? ",font="calibri")
l31.place(x=50,y=420)
m31 = Radiobutton(w, text="  1995", font='calibri', variable=mv3, value=1)
m31.place(x=75, y=460)
m32 = Radiobutton(w, text="  1972", font='calibri', variable=mv3, value=2)
m32.place(x=280, y=460)
m33 = Radiobutton(w, text="  1981", font='calibri', variable=mv3, value=3)
m33.place(x=75, y=500)
m34 = Radiobutton(w, text="  1989", font='calibri', variable=mv3, value=4)
m34.place(x=280, y=500)


mv4 = IntVar()
l41=Label(w,text="4) In which language is Python written? ",font="calibri")
l41.place(x=50,y=570)
m41 = Radiobutton(w, text="  English", font='calibri', variable=mv4, value=1)
m41.place(x=75, y=610)
m42 = Radiobutton(w, text="  PHP", font='calibri', variable=mv4, value=2)
m42.place(x=280, y=610)
m43 = Radiobutton(w, text="  C", font='calibri', variable=mv4, value=3)
m43.place(x=75, y=650)
m44 = Radiobutton(w, text="  All of the Above", font='calibri', variable=mv4, value=4)
m44.place(x=280, y=650)


parent=tk.Label

canvas = tk.Canvas(parent)
scroll_y = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)

frame = tk.Frame(canvas)
# group of widgets
for i in range(20):
    tk.Label(frame, text='label %i' % i).pack()
# put the frame in the canvas
canvas.create_window(0, 0, anchor='nw', window=frame)
# make sure everything is displayed before configuring the scrollregion
canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'),
                 yscrollcommand=scroll_y.set)

canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')

w.mainloop()
