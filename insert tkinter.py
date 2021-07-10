from tkinter import *

wind = Tk()
wind.title("project1")
wind.geometry("350x350")



def sq():
    data = int(e1.get())
    l3.delete(0, END)
    l3.insert(0, str(data * data))

def prime():
    n=int(e1.get())
    if n>1:
        for i in range(2,n):
            if n%i==0:
                l3.delete(0, END)
                l3.insert(0, "It is not a prime number")
                break
        else:
            l3.delete(0, END)
            l3.insert(0, "It is prime number")
    # else:
    #     l3.config(text="It is not a prime number")

def factorial():
    n=int(e1.get())
    a=2
    b=1
    if n==1:
        l3.delete(0, END)
        l3.insert(0, "1")
    else:
        while n>1:
            b=b*a
            a+=1
            n-=1
        l3.delete(0, END)
        l3.insert(0, str(b))

def armstrong():
    num =int(e1.get())
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        l3.delete(0, END)
        l3.insert(0,"Armstrong number")
    else:
        l3.delete(0, END)
        l3.insert(0, "not an Armstrong number")

def reset():
    l3.delete(0, END)
    l3.insert(0, " ")
    e1.delete(0,"end")


l1 = Label(wind, text="enter no")
l1.place(x=70, y=50)

e1 = Entry(wind, width=20)
e1.place(x=130, y=50)

b1 = Button(wind, width=20, text="square", command=sq)
b1.place(x=100, y=80)

b2 = Button(wind, width=20, text="prime", command=prime)
b2.place(x=100, y=110)

b3 = Button(wind, width=20, text="factorial",command=factorial)
b3.place(x=100, y=140)

b4 = Button(wind, width=20, text="armstrong number",command=armstrong)
b4.place(x=100, y=170)

b5 = Button(wind, width=20, text="reset",command=reset)
b5.place(x=100, y=200)

l2 = Label(wind,width=20, text="output")
l2.place(x=10, y=230)

l3=Entry(wind, width="22")
l3.place(x=110,y=230)

wind.mainloop()