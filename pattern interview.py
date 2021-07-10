# a=""
# while len(a)<5:
#     a=a+input("Enter Characters: ")
#     i=1
#     sep=8
#     while i<=len(a):
#         print(" "*sep,*a[:i],sep="   ")
#         i+=1
#         sep-=2

# a=""
# for m in range (1,6):
#     n=input("Enter Char:")
#     a=a+n
#     s=8
#     for j in range(len(a)):
#         for sp in range (s):
#             print(" ",end='')
#         s=s-2
#         i=0
#         for st in range(j+1):
#             print(a[i],end='   ')
#             i=i+1
#         print()

# n=int(input("n:"))
# a=1
# sep=n*2-2
# while a<=n:
#     if a%2==0:
#         print(" "*sep,"0   "*a)
#     else:
#         print(" "*sep,"1   "*a)
#     a+=1
#     sep-=2


pt=1
s=6
for m in range(1,5):
    for sp in range(s):
        print(" ",end="")
    s=s-2
    for p in range(m):
        print(str(pt),end="   ")
    print()
    if pt==1:
        pt=0
    else:
        pt=1