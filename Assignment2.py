from tkinter import *
from string import ascii_letters
from tkinter import messagebox

def Submit():
    if (rv.get() == 1):
        string=(Input.get()).lower()
        first = ""
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in string:
            if i in vowels:
                first = first + i.upper()
            else:
                first = first + i
                lb1.config(text=first)


    elif (rv.get() == 2):
        string = Input.get()
        words = string.split(" ")

        # word:: will reverse the word ... it willl be appleid to enteir list/array.
        newWords = [word[::-1] for word in words]
        newSentence = " ".join(newWords)
        lb1.config(text=newSentence)


# string = Input.get()
# rev = ""
# num1 = len(string);
# j = num1 - 1
# for i in range(0, num1):
#     rev = rev + string[j]
#     j = j - 1
#     lb1.config(text=rev)

    elif (rv.get() == 3):
        string = Input.get()
        third=""
        words = string.split()
        for i in words:
            a = i
            res = ''.join(sorted(a))
            third = third + str(res) + " "
            lb1.config(text=third)



    elif (rv.get() == 4):
        string = Input.get()
        a = "".join(dict.fromkeys(string))
        lb1.config(text=a)



    elif (rv.get() == 5):
        string = Input.get()
        fifth = ""
        for c in string:
            if c == " ":
                fifth = fifth + " "
            elif c in ascii_letters:
                fifth = fifth + ascii_letters[(ascii_letters.index(c) + 2) % len(ascii_letters)]
                lb1.config(text=fifth)

    else:
        messagebox.showerror("Error", "Choose any type")

wd = Tk()
wd. state("zoomed")
wd.title("Strings")
# wd.geometry("1366x720")

Label(wd,text='Strings',font=('calibri',30,'bold'),fg='blue').place(x=600,y=30)

Label(wd,text="Enter String:",font=("calibri",15,"bold")).place(x=100,y=130)
Input= Entry(wd,width=60,font=("calibri",15,"bold"),border=1,relief="solid")
Input.place(x=230,y=130)


Label(wd,text="Select Type:",font=("calibri",15,"bold")).place(x=100,y=180)

rv = IntVar()
r1 = Radiobutton(wd, text="Type-1",font=("calibri",15), variable=rv, value=1)
r1.place(x=230, y=180)

r2 = Radiobutton(wd, text="Type-2",font=("calibri",15), variable=rv, value=2)
r2.place(x=330, y=180)

r3 = Radiobutton(wd, text="Type-3",font=("calibri",15), variable=rv, value=3)
r3.place(x=430, y=180)

r4 = Radiobutton(wd, text="Type-4",font=("calibri",15), variable=rv, value=4)
r4.place(x=530, y=180)

r5 = Radiobutton(wd, text="Type-5",font=("calibri",15), variable=rv, value=5)
r5.place(x=630, y=180)

Button(wd,text='Submit',width=10, font = ("calibri",10),command = Submit,border=1,relief="solid").place(x=746,y=183)

Label(wd,text='Output:',font=("calibri",20)).place(x=100,y=240)
lb1 = Label(wd,text="Enter String & select a type to get output",font = ("calibri",15))
lb1.place(x=100,y=290)

wd.mainloop()