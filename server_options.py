import socket
s=socket.socket()
h="localhost"
p=54323

ad=(h,p)
s.bind(ad)
s.listen(2)
def fact(n):
    a = 1
    f = 1
    while a<n:
        f+=f*a
        a+=1
    return f


def prime(n):
    for i in range(2,n):
        if n%i==0:
            return ("Not prime number")
        break
    else:
        return ("Prime number")

def Fib(n):

    if n < 0:
        return("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return Fib(n - 1) + Fib(n - 2)

while True:
    conn,addrs=s.accept()
    print("connection")
    m = "1.Prime/n2.Factorial/n3.fibonacci(using recurssion)/n Enter(1|2|3)"
    conn.send(m.encode())

    op=conn.recv(128)
    op=int(op)

    n = conn.recv(128)
    n = int(n)

    if op==1:
        o=prime(n)
        conn.send(o.encode())
    if op==2:
        o=fact(n)
        o = str(o)
        conn.send(o.encode())
    if op==3:
        o=Fib(n)
        o = str(o)
        conn.send(o.encode())

    conn.close()