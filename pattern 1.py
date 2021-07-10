s=8
for i in range(1,6):
    print(" "*s,end="")
    for j in range (1,i+1):
        if i==2:
            print(*("1"*i),sep="   ",end="")
            break
        if i==4:
            print(*("0"*i),sep="   ",end="")
            break
        print(chr(64+j),end="   ")
    s-=2
    print()