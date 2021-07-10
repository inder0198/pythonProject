from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as m
conn=m.connect(user="root",password="root",host="localhost",database="inder")
cur=conn.cursor()

wind=Tk()
wind.title("Registration Form")
wind.geometry("600x500")

def reset():
    e1.delete("0","end")
    e2.delete("0","end")
    e3.delete("0","end")
    e4.delete("0","end")
    e9.delete("0.1","end")
    rv.set(0)
    rv1.set(0)
    cv1.set(0)
    cv2.set(0)
    cv3.set(0)
    cb.current(0)

def store():
    fn=e1.get()
    ln=e2.get()
    cn=e3.get()
    em=e4.get()
    if cb.get() != "Select your Age":
        ag = cb.get()
    else:
        cb.current(0)
    ad=e9.get("0.1","end")
    ad=ad.replace("\n","")
    # c1=cv1.get()
    # c2=cv2.get()
    # c3=cv3.get()
    if (rv.get()==1):
        gn="Male"
    elif(rv.get()==2):
        gn="Female"
    elif(rv.get()==3):
        gn="Others"
    else:
        messagebox.showerror("Error","Choose gender")

    if (rv1.get()==1):
        qf="10th"
    elif(rv1.get()==2):
        qf="12th"
    elif(rv1.get()==3):
        qf="Degree"
    else:
        messagebox.showerror("Error","Enter Qualification")


    hobby=""
    if cv1.get()==1:
        hobby = hobby + " Playing"
    if cv2.get()==1:
        hobby = hobby + " Singing"
    if cv3.get()==1:
        hobby = hobby + " Reading"
    if cv1.get()==0 and cv2.get()==0 and cv3.get()==0:
        messagebox.showerror("Error","Please select hobby")



    #
    # data=[]
    #
    # data.append(fn)
    # data.append(ln)
    # data.append(cn)
    # data.append(em)
    # data.append(gn)
    # data.append(hobby)
    # data.append(qf)
    # data.append(ag)
    # data.append(ad)
    #
    # print(*data)

    print(fn,ln,cn,em,gn,hobby,qf,ag,ad)

    v=(fn,ln,cn,em,gn,hobby,qf,ag,ad)
    q="insert into forms(fname,lname,contact,email,gender,hobby,qualification,age,address) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(q,v)
    conn.commit()

rv=IntVar()
rv1=IntVar()
cv1=IntVar()
cv2=IntVar()
cv3=IntVar()

l1=Label(wind,text="F_Name:")
l1.place(x=10,y=10)

e1=Entry(wind,width=20)
e1.place(x=65,y=8)

l2=Label(wind,text="L_Name:")
l2.place(x=250,y=10)

e2=Entry(wind,width=20)
e2.place(x=305,y=8)

l3=Label(wind,text="Cont_no:")
l3.place(x=10,y=40)

e3=Entry(wind,width=20)
e3.place(x=65,y=38)

l4=Label(wind,text="Email_Id:")
l4.place(x=250,y=40)

e4=Entry(wind,width=20)
e4.place(x=305,y=38)

l5=Label(wind,text="Gender:")
l5.place(x=10,y=70)

r1=Radiobutton(wind,text="Male",variable=rv,value=1)
r1.place(x=60,y=68)

r2=Radiobutton(wind,text="Female",variable=rv,value=2)
r2.place(x=60,y=98)

r3=Radiobutton(wind,text="Other",variable=rv,value=3)
r3.place(x=60,y=128)

l6=Label(wind,text="Hobby:")
l6.place(x=250,y=70)

c1=Checkbutton(wind,text="Playing",variable=cv1,onvalue=1,offvalue=0)
c1.place(x=300,y=68)

c2=Checkbutton(wind,text="Singing",variable=cv2,onvalue=1,offvalue=0)
c2.place(x=300,y=98)

c3=Checkbutton(wind,text="Reading",variable=cv3,onvalue=1,offvalue=0)
c3.place(x=300,y=128)

l7=Label(wind,text="Qualification:")
l7.place(x=10,y=160)

r4=Radiobutton(wind,text="10th",variable=rv1,value=1)
r4.place(x=90,y=158)

r5=Radiobutton(wind,text="12th",variable=rv1,value=2)
r5.place(x=90,y=188)

r6=Radiobutton(wind,text="Degree",variable=rv1,value=3)
r6.place(x=90,y=218)

l8=Label(wind,text="Age:")
l8.place(x=10,y=250)
age=[i for i in range(20,41)]
age.insert(0,"Select your age")
cb=ttk.Combobox(wind,width=15)
cb['value']=age
cb.place(x=80,y=248)
cb.current(0)

l9=Label(wind,text="Address:")
l9.place(x=250,y=160)
e9=Text(wind,height=5,width=25)
e9.place(x=305,y=160)

b1=Button(wind,text="Submit",command=store)
b1.place(x=220,y=300)

# l10=Label(wind,text="")
# l10.place(x=200,y=270)

b2=Button(wind,text="Reset",command=reset)
b2.place(x=220,y=350)

wind.mainloop()

# mysql> create table form (fname varchar(30), lname varchar(30), contact bigint, email varchar (30),gender varchar(7),hobby varchar(40),qualification varchar (20),age int(7),address varchar(400));

    # def login():
    #     q1="use regdb"
    #     cur.execute(q1)
    #     data=[]
    #     username=e1.get()
    #     password=e2.get()
    #     data.append(username)
    #     data.append(password)
    #     data=tuple(data)
    #     v=(username,password)
    #     q2="select username,password from regdb where username=%s or password=%s"
    #     cur.execute(q2,v)
    #     dbdata=cur.fetchall()
    #     if dbdata[0][0]==username and dbdata[0][1]password:
    #         form()
    #     if dbdata[0][0]==username and dbdata[0][1]!=password:
    #         messagebox.showerror("message","incorrect password")
    #     if dbdata[0][0]!=username and dbdata[0][1]==password:
    #         messagebox.showerror("message","incorrect username")
    #     if dbdata[0][0]!=username and dbdata[0][1]==password:
    #         messagebox.showerror("message","user does not exist")
