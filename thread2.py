import threading
import time


def fact():
    n=10
    a = 0
    f = 1
    while a<n:
        f+=f*a
        a += 1
        print("Factorial of",a,"is",f)
        time.sleep(2)


def prime():
    n = 10
    for i in range(1,n+1):
        if i==2:
            result=(i,"is prime number")
        elif i==3:
            result=(i,"is Prime number")
        elif i%2==0 or i%3==0:
            result=(i,"is not prime number")
        else:
            result=(i,"is prime number")
        print(*result)
        time.sleep(2)


def Fib(n):
    l=[0,1]
    for i in range(1,n+1):
        if i==1 or i==2:
            print("Fibonacci of",i,"is",*l[:i])
            time.sleep(2)
        else:
            f=l[-1]+l[-2]
            l.append(f)
            print("Fibonacci of",i,"is",*l,sep=" ")
            time.sleep(2)


t1 = threading.Thread(target=prime,)
t2 = threading.Thread(target=fact, )
t3 = threading.Thread(target=Fib,args=(10,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()