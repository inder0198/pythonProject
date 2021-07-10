from tkinter import *
from tkinter import messagebox

def click(event):
    text=event.widget.cget("text")
    print(text)

wd1=Tk()
wd1.geometry("247x330")
wd1.title("Calculator")
wd1.resizable(0,0)

e1=Entry(wd1,width=16,font="calibri 20 bold",border=1,relief="solid",justify=RIGHT)
e1.place(x=10,y=10)

#1st row
b1=Button(wd1,text="C",border=1,relief="solid",font="calibri 13")
b1.place(x=10,y=50,width=50,height=50)
b1.bind("<Button-1>",click)

b2=Button(wd1,text="+/-",border=1,relief="solid",font="calibri 13")
b2.place(x=70,y=50,width=50,height=50)
b2.bind("<Button-1>",click)

b3=Button(wd1,text="%",border=1,relief="solid",font="calibri 13")
b3.place(x=128,y=50,width=50,height=50)
b3.bind("<Button-1>",click)

b4=Button(wd1,text="÷",border=1,relief="solid",font="calibri 13")
b4.place(x=187,y=50,width=50,height=50)
b4.bind("<Button-1>",click)

#2nd row
b5=Button(wd1,text="7",border=1,relief="solid",font="calibri 13")
b5.place(x=10,y=105,width=50,height=50)
b5.bind("<Button-1>",click)

b6=Button(wd1,text="8",border=1,relief="solid",font="calibri 13")
b6.place(x=70,y=105,width=50,height=50)
b6.bind("<Button-1>",click)

b7=Button(wd1,text="9",border=1,relief="solid",font="calibri 13")
b7.place(x=128,y=105,width=50,height=50)
b7.bind("<Button-1>",click)

b8=Button(wd1,text="X",border=1,relief="solid",font="calibri 13")
b8.place(x=187,y=105,width=50,height=50)
b8.bind("<Button-1>",click)

#3rd row
b9=Button(wd1,text="4",border=1,relief="solid",font="calibri 13")
b9.place(x=10,y=160,width=50,height=50)
b9.bind("<Button-1>",click)

b10=Button(wd1,text="5",border=1,relief="solid",font="calibri 13")
b10.place(x=70,y=160,width=50,height=50)
b10.bind("<Button-1>",click)

b11=Button(wd1,text="6",border=1,relief="solid",font="calibri 13")
b11.place(x=128,y=160,width=50,height=50)
b11.bind("<Button-1>",click)

b12=Button(wd1,text="-",border=1,relief="solid",font="calibri 13")
b12.place(x=187,y=160,width=50,height=50)
b12.bind("<Button-1>",click)

#4th row
b13=Button(wd1,text="1",border=1,relief="solid",font="calibri 13")
b13.place(x=10,y=215,width=50,height=50)
b13.bind("<Button-1>",click)

b14=Button(wd1,text="2",border=1,relief="solid",font="calibri 13")
b14.place(x=70,y=215,width=50,height=50)
b14.bind("<Button-1>",click)

b15=Button(wd1,text="3",border=1,relief="solid",font="calibri 13")
b15.place(x=128,y=215,width=50,height=50)
b15.bind("<Button-1>",click)

b16=Button(wd1,text="+",border=1,relief="solid",font="calibri 13")
b16.place(x=187,y=215,width=50,height=50)
b16.bind("<Button-1>",click)

#5th row
b17=Button(wd1,text="0",border=1,relief="solid",font="calibri 13")
b17.place(x=10,y=270,width=50,height=50)
b17.bind("<Button-1>",click)

b18=Button(wd1,text=".",border=1,relief="solid",font="calibri 13")
b18.place(x=70,y=270,width=50,height=50)
b18.bind("<Button-1>",click)

b19=Button(wd1,text="del",border=1,relief="solid",font="calibri 13")
b19.place(x=128,y=270,width=50,height=50)
b19.bind("<Button-1>",click)

b20=Button(wd1,text="=",border=1,relief="solid",font="calibri 13")
b20.place(x=187,y=270,width=50,height=50)
b20.bind("<Button-1>",click)

wd1.mainloop()


# global outputvalue
#
# outputvalue = Stringvar ()
# outputvalue.set("")
#
#     if text == "=":
#         pass
#     else:
#         text == "C"
#         outputvalue.set("")
#         outputvalue.update()