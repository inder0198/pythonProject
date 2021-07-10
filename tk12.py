from tkinter import *
from tkinter import ttk

def stored():
    fn=e1.get()
    ls=e2.get()
    cn=e3.get()
    ml=e4.get()
    # ql=e5.get()
    ag=cb.get()
    ad=e6.get("0.1","end")

    if (rv.get()==1):
        gn="Male"
    elif(rv.get()==2):
        gn="Female"
    elif(rv.get()==3):
        gn="Others"
    else:
        gn="choose gender"



    print(fn,ls,cn,gn,ml,ag,ad)




win=Tk()
win.geometry("500x400")

rv=IntVar()
rv1=IntVar()
cv1=IntVar()
cv2=IntVar()
cv3=IntVar()



l1=Label(win,text="First Name").place(x=10,y=15)
e1=Entry(win,width=15)
e1.place(x=100,y=15)

l2=Label(win,text="Last Name").place(x=250,y=15)
e2=Entry(win,width=15)
e2.place(x=330,y=15)

l3=Label(win,text="Contact No").place(x=10,y=40)
e3=Entry(win,width=15)
e3.place(x=100,y=40)

l4=Label(win,text="Mail").place(x=250,y=40)
e4=Entry(win,width=15)
e4.place(x=330,y=40)

l5=Label(win,text="Gender").place(x=10,y=70)
r1=Radiobutton(win,text="Male",variable=rv,value=1)
r1.place(x=30,y=90)
r2=Radiobutton(win,text="Female",variable=rv,value=2)
r2.place(x=30,y=120)
r3=Radiobutton(win,text="Others",variable=rv,value=3)
r3.place(x=30,y=150)

l6=Label(win,text="Hobbies").place(x=230,y=70)
c1=Checkbutton(win,text="playing",variable=cv1,onvalue=1,offvalue=0)
c1.place(x=250,y=90)
c2=Checkbutton(win,text="singing",variable=cv2,onvalue=1,offvalue=0)
c2.place(x=250,y=120)
c3=Checkbutton(win,text="reading",variable=cv3,onvalue=1,offvalue=0)
c3.place(x=250,y=150)

l7=Label(win,text="Qualifications").place(x=10,y=180)
rq1=Radiobutton(win,text="10th",variable=rv1,value=1)
rq1.place(x=50,y=200)
rq2=Radiobutton(win,text="12th",variable=rv1,value=2)
rq2.place(x=50,y=220)
rq3=Radiobutton(win,text="degree",variable=rv1,value=3)
rq3.place(x=50,y=240)



l7=Label(win,text="Age").place(x=10,y=280)
age=[i for i in range(20,40)]
cb=ttk.Combobox(win,width=10)
cb['value']=age
cb.place(x=70,y=280)
cb.current(0)

l8=Label(win,text="Address").place(x=280,y=220)
e6=Text(win,height=4,width=20)
e6.place(x=320,y=250)

b1=Button(win,text="Submit",command=stored)
b1.place(x=200,y=320)

win.mainloop()