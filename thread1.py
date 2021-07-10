import time
import threading


def a1():
    for i in range(10):
        print("s1",i)
        time.sleep(1)
def a2():
    for i in range(10):
        print("s2",i)
        time.sleep(1)

t1=threading.Thread(target=a1,)
t2=threading.Thread(target=a2,)

t1.start()
t2.start()

t1.join()
t2.join()