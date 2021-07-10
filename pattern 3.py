n=4
s=n*2
v=64
for i in range(1,n+1):
    print(" "*s,end="")
    for j in range(1,i+1):
        if j==1:
            print("A",end="   ")
        if j==2:
            print("b",end="   ")
        if j>2:
            print(chr(v+j),end="   ")
    s=s-2
    print()