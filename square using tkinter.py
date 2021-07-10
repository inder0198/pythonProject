from tkinter import *
wind=Tk()
wind.title("project1")
wind.geometry("300x300")


def sq():
	data=int(e1.get())
	l2.config(text=str(data*data))
	

l1=Label(wind,text="enter no")
l1.place(x=50,y=150)

e1=Entry(wind,width=15)
e1.place(x=250,y=150)

b1=Button(wind,text="square",command=sq)
b1.place(x=200,y=300)

l2=Label(wind,text="output")
l2.place(x=250,y=400)


wind.mainloop()