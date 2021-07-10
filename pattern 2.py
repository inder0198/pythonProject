b=1
sp=8
l=[]
for i in range (1,6):
    temp=""
    a=1
    for j in range (1,i+1):
        if j%2!=0:
            temp=temp+(chr(64+a))
            a+=1
        if j==2:
            temp=temp+"1"
        if j==4:
            temp=temp+"0"
    l.append(temp)
for i in l:
    print(" "*sp,end="")
    print(*i,sep="   ")
    sp-=2
