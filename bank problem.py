#bank problem
class bank:
    def __init__(self):
        self.bal=150000
    def withdraw(self):
        if amt>self.bal:
            print("insufficient balance")
        elif amt>100000:
            print("cannot withdraw more than 100000rs")
        elif amt<=self.bal:
            self.bal-=amt
        print('balance:',self.bal)
    def deposit(self):
        if amt>100000:
            print("cannot deposit more than 100000rs")
        elif amt<100000:
            self.bal+=amt
        print('balance:',self.bal)

obj=bank()
a=input("enter opeartion name:")
amt=int(input("enter amount:"))
if a=="withdraw":
    x=obj.withdraw()
elif a=="deposit":
    x=obj.deposit()
x
