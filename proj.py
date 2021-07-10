from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as m
conn = m.connect(user="root", password="root", host="localhost", database="inder")
cur = conn.cursor()

def form():
    q10="select * from forms"
    cur.execute(q10)
    count=cur.fetchall()
    count=60-len(count)

    wd3 = Tk()
    wd3.title("Form " + "(Available seats = " + str(count) + ")")
    wd3.geometry("350x550")
    wd3.resizable(0, 0)


    cv1 = IntVar()
    cv2 = IntVar()
    cv3 = IntVar()

    l10 = Label(wd3, text="F_Name:")
    l10.place(x=10, y=10)

    e10 = Entry(wd3, width=35)
    e10.place(x=100, y=8)

    l11 = Label(wd3, text="L_Name:")
    l11.place(x=10, y=50)

    e11 = Entry(wd3, width=35)
    e11.place(x=100, y=48)

    l12 = Label(wd3, text="Cont_no:")
    l12.place(x=10, y=90)

    e12 = Entry(wd3, width=35)
    e12.place(x=100, y=88)

    l13 = Label(wd3, text="Email_Id:")
    l13.place(x=10, y=130)

    e13 = Entry(wd3, width=35)
    e13.place(x=100, y=128)

    l14 = Label(wd3, text="Gender:")
    l14.place(x=10, y=180)

    rv = IntVar()
    r1 = Radiobutton(wd3, text="Male", variable=rv, value=1)
    r1.place(x=100, y=178)

    r2 = Radiobutton(wd3, text="Female", variable=rv, value=2)
    r2.place(x=170, y=178)

    r3 = Radiobutton(wd3, text="Other", variable=rv, value=3)
    r3.place(x=240, y=178)

    l15 = Label(wd3, text="Hobby:")
    l15.place(x=10, y=230)

    c1 = Checkbutton(wd3, text="Playing", variable=cv1, onvalue=1, offvalue=0)
    c1.place(x=100, y=228)

    c2 = Checkbutton(wd3, text="Singing", variable=cv2, onvalue=1, offvalue=0)
    c2.place(x=170, y=228)

    c3 = Checkbutton(wd3, text="Reading", variable=cv3, onvalue=1, offvalue=0)
    c3.place(x=240, y=228)

    l16 = Label(wd3, text="Qualification:")
    l16.place(x=10, y=280)

    rv1 = IntVar()
    r4 = Radiobutton(wd3, text="10th", variable=rv1, value=1)
    r4.place(x=100, y=278)

    r5 = Radiobutton(wd3, text="12th", variable=rv1, value=2)
    r5.place(x=170, y=278)

    r6 = Radiobutton(wd3, text="Degree", variable=rv1, value=3)
    r6.place(x=240, y=278)

    l8 = Label(wd3, text="Age:")
    l8.place(x=10, y=320)

    age = [i for i in range(20, 41)]
    age.insert(0, "Select your age")
    cb = ttk.Combobox(wd3, width=15)
    cb['value'] = age
    cb.place(x=100, y=318)
    cb.current(0)

    l17 = Label(wd3, text="Address:")
    l17.place(x=10, y=370)
    e17 = Text(wd3, height=5, width=25)
    e17.place(x=100, y=368)

    def store():
        if count<=0:
            messagebox.showinfo("Message","No seats available")
        else:

            data=[]
            if len(e10.get())==0:
                messagebox.showerror("error","Enter F_Name")
            else:
                fn = e10.get()
                data.append(fn)

            if len(e11.get())==0:
                messagebox.showerror("error","Enter L_Name")
            else:
                ln = e11.get()
                data.append(ln)

            try:
                if len(e12.get())==10:
                    cn = int(e12.get())
                    data.append(cn)
                if 0<len(e12.get())<10 or len(e12.get())>10:
                    messagebox.showerror("error","Contact number should be 10 digit")
            except:
                messagebox.showerror("error","Enter Contact")


            if len(e12.get())==0:
                messagebox.showerror("error","Enter Email ID")
            else:
                em = e13.get()
                data.append(em)

            if (rv.get() == 1):
                gn = "Male"
                data.append(gn)
            elif (rv.get() == 2):
                gn = "Female"
                data.append(gn)
            elif (rv.get() == 3):
                gn = "Others"
                data.append(gn)
            else:
                messagebox.showerror("Error", "Choose Gender")

            hobby = ""
            if cv1.get() == 1:
                hobby = hobby + "Playing"
            if cv2.get() == 1:
                hobby = hobby + " Singing"
            if cv3.get() == 1:
                hobby = hobby + " Reading"
            if cv1.get() == 0 and cv2.get() == 0 and cv3.get() == 0:
                messagebox.showerror("Error", "Please select Hobby")
            hobby=hobby
            data.append(hobby)

            if (rv1.get() == 1):
                qf = "10th"
                data.append(qf)
            elif (rv1.get() == 2):
                qf = "12th"
                data.append(qf)
            elif (rv1.get() == 3):
                qf = "Degree"
                data.append(qf)
            else:
                messagebox.showerror("Error", "Enter Qualification")

            if cb.get() == "Select your age":
                messagebox.showerror("Error", "select Age")
            else:
                # cb.current(0)
                ag = int(cb.get())
                data.append(ag)

            adr=e17.get("0.1","end")
            adr=adr.replace("\n","")
            if adr=="":
                messagebox.showerror("error","Enter Address")
            else:
                ad = e17.get("0.1", "end")
                ad = ad.replace("\n", "")
                data.append(ad)

            # print(fn, ln, cn, em, gn, hobby, qf, ag, ad)
            # v = (fn,ln,cn,em,gn,hobby,qf,ag,ad)
            data=tuple(data)
            print(data)
            q5 = "select fname,lname,contact,email,gender,hobby,qualification,age,address from forms"
            cur.execute(q5)
            temp1=cur.fetchall()
            print(temp1)
            if data in temp1:
                messagebox.showinfo("Message","your data is already stored")
            else:
                v=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])
                q = "insert into forms(fname,lname,contact,email,gender,hobby,qualification,age,address) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(q,v)
                conn.commit()
                messagebox.showinfo("Message","Your data is successfully saved")
            wd3.destroy()


    b4 = Button(wd3, text="Submit", command=store)
    b4.place(x=150, y=500)

    wd3.mainloop()


def home():

    wd1 = Tk()
    wd1.title("Login")
    wd1.geometry("300x150")
    wd1.resizable(0, 0)

    #login page
    l1=Label(wd1,text="User name:")
    l1.place(x=10,y=20)

    e1=Entry(wd1,width=30)
    e1.place(x=85,y=18)

    l2=Label(wd1,text="Password:")
    l2.place(x=10,y=60)

    e2=Entry(wd1,show="*",width=30)
    e2.place(x=85,y=58)

    def register():
        wd1.destroy()
        wd2 = Tk()
        wd2.title("Register")
        wd2.geometry("300x250")
        wd2.resizable(0, 0)

        l5 = Label(wd2, text="User name:")
        l5.place(x=10, y=20)

        e5 = Entry(wd2, width=30)
        e5.place(x=85, y=18)

        l6 = Label(wd2, text="Password:")
        l6.place(x=10, y=60)

        e6 = Entry(wd2, show="*", width=30)
        e6.place(x=85, y=58)

        l7 = Label(wd2, text="Contact no:")
        l7.place(x=10, y=100)

        e7 = Entry(wd2, width=30)
        e7.place(x=85, y=98)

        l8 = Label(wd2, text="Email-ID:")
        l8.place(x=10, y=140)

        e8 = Entry(wd2, width=30)
        e8.place(x=85, y=138)

        def regdb():
            q="select * from regdb"
            cur.execute(q)
            temp=cur.fetchall()
            users=list(x[0] for x in temp)

            username=e5.get()
            if username in users:
                messagebox.showerror("Error","Username already exist")
            password=e6.get()
            try:
                if len(e7.get()) == 10:
                    contact = int(e7.get())
                if 0 < len(e7.get()) < 10 or len(e7.get()) > 10:
                    messagebox.showerror("error", "Contact number should be 10 digit")
            except ValueError:
                messagebox.showerror("error", "enter Contact")

            email=e8.get()

            print(username, password, contact,email)

            v = (username,password,contact,email)
            q = "insert into regdb(username,password,contact,email) values (%s,%s,%s,%s)"
            cur.execute(q, v)
            conn.commit()
            wd2.destroy()
            home()

        b3 = Button(wd2, text="Submit", command=regdb)
        b3.place(x=125, y=180)

        wd2.mainloop()
    def login():
        data=[]
        username=e1.get()
        password=e2.get()
        data.append(username)
        data.append(password)
        v=(username,password)
        q2="select username,password from regdb where username=%s or password=%s"
        cur.execute(q2,v)
        dbdata=cur.fetchall()
        try:
            if dbdata[0][0]==username and dbdata[0][1]==password:
                wd1.destroy()
                form()
            if dbdata[0][0] == username and dbdata[0][1] != password:
                messagebox.showerror("error","incorrect password")
            if dbdata[0][0] != username and dbdata[0][1] == password:
                messagebox.showerror("error","incorrect username")
        except IndexError:
                messagebox.showerror("error","user does not exist")

    b1=Button(wd1,text="Login",command=login) #command=lambda:[wd1.destroy(),login()]
    b1.place(x=100,y=110)

    b2=Button(wd1,text="Register",command=register)
    b2.place(x=150,y=110)

    wd1.mainloop()

home()