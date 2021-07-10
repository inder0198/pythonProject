n=int(input("No of matrices:"))
row=int(input("rows:"))
col=int(input("columns:"))
matrix={}
for k in range(n):
    m1=[]
    k=str(k)
    a="l"+k
    for i in range(row):
        temp=[]
        for j in range(col):
            a=int(input("enter elements:"))
            temp.append(a)
            m1.append(temp)
            matrix[a]=m1
print(matrix)