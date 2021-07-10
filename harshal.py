import time
import threading
# def a1():
#     for i in range(5):
#         print("s1",i)
#         time.sleep(1)
#
# def a2():
#     for i in range(9):
#         print("s2",i)
#         time.sleep(2)
def fact():
    n=10
    a = 0
    f = 1
    while a < n:
        f += f * a
        a += 1
        print("Factorial of",a,"is:",f)
        time.sleep(1)
def prime():
    n=10
    for i in range(1, n+1):
        if i==2:
            result=i,"is not prime number"
        elif i==3:
            result=i,"is prime number"
        elif i%2 == 0 or i%3==0:
            result=i,"is Not prime number"
        else:
            result=i,"is Prime number"
        print(*result)
        time.sleep(1)


def fib(n):
    l=[0,1]

    for i in range(1,n+1):
        if i == 1 or i == 2:
            print("Fibonnacci of",i,"is:",*l[:i])
            time.sleep(1)
        else:
            f = l[-1] + l[-2]
            l.append(f)
            print("Fibonnacci of", i, "is:", *l, sep=" ")
            time.sleep(1)

t1 = threading.Thread(target=prime, )
t2 = threading.Thread(target=fact, )
t3 = threading.Thread(target=fib, args=(10,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()