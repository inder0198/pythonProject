from tkinter import *
from tkinter import ttk
import mysql.connector as m
conn=m.connect(user="root",password="root",host="localhost",database="inder")
cur=conn.cursor()


win = Tk()
win.title("Registration Form")
win.geometry("900x900")
win.configure(bg='light blue')
win.resizable(0,0)
data=[]
def reg():

    fname=fn2.get()
    lname=ln2.get()
    contact=cn2.get()
    email=em2.get()
    if cb.get()!="Select your Age":
        age=cb.get()
    else:
        cb.current(0)

    address=add1.get("0.1","end")

    data.append(fname)
    data.append(lname)
    data.append(contact)
    data.append(email)

# gender
    if (rv.get()==1):
        gender="Male"
    elif(rv.get()==2):
        gender="Female"
    elif(rv.get()==3):
        gender="Other"
    else:
        lj.config(text="select gender")
    data.append(gender)
# qualification
    if(qv1.get()==1):
        qualification="10th"
    elif (qv1.get() == 2):
        qualification = "12th"
    elif (qv1.get() == 3):
        qualification = "Diploma"
    elif (qv1.get() == 4):
        qualification = "Enggineering"

    else:
        lm.config(text="Select Qualification")
    data.append(qualification)

# hobbies
    hobby=""
    if (cv1.get() == 1):
        hobby = hobby +" Playing"
    if (cv2.get() == 1):
        hobby = hobby +" Singing"
    if (cv3.get() == 1):
        hobby = hobby +" Bike Riding"
    if(cv1.get()==0) and (cv2.get()==0) and (cv3.get()==0):
        lk.config(text="Select Your Hobby")
    data.append(hobby)

    data.append(age)
    data.append(address)

    print(data)

    v=(fname,lname,contact,email,gender,age,hobby,qualification,address)
    q="insert into form values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(q,v)
    conn.commit()

def reset():

    fn2.delete(0, END)
    ln2.delete(0,END)
    cn2.delete(0,END)
    em2.delete(0,END)
    add1.delete(0.1, END)
    cb.current(0)
    qv1.set(0)
    rv.set(0)
    cv1.set(0)
    cv2.set(0)
    cv3.set(0)

tt=Label(win,text="Registration Form",font='helvetica',border=1,relief='sunken')
tt.place(x=400,y=5)
fn1=Label(win,text="First Name :",bg="light blue")
fn1.place(x=30,y=50)
fn2=Entry(win,width=40,border=1,relief='solid')
fn2.place(x=130,y=50)

ln1=Label(win,text="Last Name",bg="light blue")
ln1.place(x=30,y=110)
ln2=Entry(win,width=40,border=1,relief='solid')
ln2.place(x=130,y=110)

cn1=Label(win,text="Contact No",bg="light blue")
cn1.place(x=30,y=170)
cn2=Entry(win,width=40,border=1,relief='solid')
cn2.place(x=130,y=170)

em1=Label(win,text="Email ID",bg="light blue")
em1.place(x=30,y=230)
em2=Entry(win,width=40,border=1,relief='solid')
em2.place(x=130,y=230)

# Radiobutton
rv=IntVar()
gen=Label(win,text="Gender",bg="light blue")
gen.place(x=30,y=290)
r1=Radiobutton(win,text="   Male",variable=rv,value=1,bg="light blue")
r1.place(x=130,y=290)
r2=Radiobutton(win,text="   Female",variable=rv,value=2,bg="light blue")
r2.place(x=130,y=320)
r3=Radiobutton(win,text="   Other",variable=rv,value=3,bg="light blue")
r3.place(x=130,y=350)

# Checkbox
cv1=IntVar()
cv2=IntVar()
cv3=IntVar()
ho=Label(win,text="Hobbies",bg="light blue")
ho.place(x=30,y=410)
c1=Checkbutton(win,text="   Playing",variable=cv1,onvalue=1,offvalue=0,bg="light blue")
c1.place(x=130,y=410)
c2=Checkbutton(win,text="   Singing",variable=cv2,onvalue=1,offvalue=0,bg="light blue")
c2.place(x=130,y=440)
c3=Checkbutton(win,text="   Bike Riding",variable=cv3,onvalue=1,offvalue=0,bg="light blue")
c3.place(x=130,y=470)

# Qualification
q=Label(win,text="Qualification",bg="light blue")
q.place(x=30,y=530)
qv1=IntVar()
q1=Radiobutton(win,text="   10th",variable=qv1,value=1,bg="light blue")
q1.place(x=130,y=530)
q2=Radiobutton(win,text="   12th",variable=qv1,value=2,bg="light blue")
q2.place(x=130,y=560)
q3=Radiobutton(win,text="   Diploma",variable=qv1,value=3,bg="light blue")
q3.place(x=130,y=590)
q4=Radiobutton(win,text="   Enggineering",variable=qv1,value=4,bg="light blue")
q4.place(x=130,y=620)

# Dropdown Menu
dd=Label(win,text="Age",bg="light blue").place(x=460,y=290)
age=[i for i in range(20,41)]
age.insert(0,"Select your Age")
cb=ttk.Combobox(win,width=20)
cb['value']=age
cb.place(x=560,y=290)
cb.current(0)

# textfield
add=Label(win,text="Address",bg="light blue").place(x=460,y=350)
add1=Text(win,width=25,height=4,border=1,relief='solid')
add1.place(x=560,y=350)
b1=Button(win,text="Submit",command=reg,width=20)
b1.place(x=200,y=700)

lj=Label(win,text=" ",bg="light blue")
lj.place(x=220,y=290)

lk=Label(win,text=" ",bg="light blue")
lk.place(x=220,y=410)

lm=Label(win,text=" ",bg="light blue")
lm.place(x=220,y=530)

b5 = Button(win, text="Reset", command=reset,width=20)
b5.place(x=350, y=700)

b6 = Button(win, text="Quit", command=win.destroy,width=20)
b6.place(x=500, y=700)

win.mainloop()