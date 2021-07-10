# Interview question python pattern

# n = int(input("no of rows:"))
# a = n*2-2
# b = 4
# d=n
# for i in range(1,2):
#     print(" "*(n*2),end="")
#     for j in range(i):
#         print(chr(64+n))
#
# for i in range(1,n-1):
#     print(" "*a,end="")
#     a-=2
#     k = 63+n
#     for j in range(i+1):
#         print(chr(k-j),end="   ")
#     print()
# print(" "*1,"A   "*n)
#
# for i in range(n-1,1,-1):
#     print(" "*b,end="")
#     b+=2
#     k = 65
#     for j in range(i,0,-1):
#         print(chr(k+j),end="   ")
#     print()
# print(" "*(n*2-1),"A")


# store factorial from 1 to 10 and store in a file

# n=int(input("n:"))
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n * fact(n-1)
# f=open("fact1.txt","a")
# for i in range(1,n+1):
#     print(fact(i))
#     a=f.write(str(fact(i))+"\n")
# f.close()
#print(f.read("fact.txt"))
