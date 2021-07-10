year=int(input("enter year:"))
a= year // 100
b= year % 100
if b==0:
    print(a, "century")
else:
    print(a+1,"century")