import socket
s=socket.socket()
h="localhost"
p=54323

ad=(h,p)
s.connect(ad)
print(s.recv(128))

op=input("Enter(1|2|3):")
s.send(op.encode())

n=input("n:")
s.send(n.encode())

print(s.recv(128))
s.close()