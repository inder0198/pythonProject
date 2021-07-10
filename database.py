import mysql.connector as m
conn=m.connect(user='root',password='root',host='localhost',database='harshal')
cur=conn.cursor()
x=0
while x==0:
    op=input("enter operation name(add|update|delete|view):")

    #data insertion
    if op=="add":
        q="insert into employee (id,name,salary) values(%s,%s,%s)"
        v=[]
        for i in range(int(input("no of inputs:"))):
            a=[]
            id=int(input("id:"))
            a.append(id)
            name=input("name:")
            a.append(name)
            salary=int(input("salary:"))
            a.append(salary)
            a=tuple(a)
            print(a)
            v.append(a)
            print()
        cur.executemany(q, v)

    # data update
    elif op=="update":
        a=input("which column u want to update:")
        if a=="name":
            s = input("name:")
            id = int(input("id:"))
            v = (s, id)
            q = ("update employee set name=%s where id=%s")
            cur.execute(q, v)
        if a=="salary":
            s=int(input("salary:"))
            id=int(input("id:"))
            v=(s,id)
            q=("update employee set salary=%s where id=%s")
            cur.execute(q, v)

    # data deletion
    elif op=="delete":
        a = input("how much u want to delete(one|all):")
        if a == "all":
            v=(input("table name:"))
            q = ("delete from "+v)
            cur.execute(q)
        if a=="one":
            name=input("name:")
            id=int(input("id:"))
            v=(name,id)
            q = ("delete from employee where name=%s and id=%s")
            cur.execute(q,v)

    # view data
    elif op=="view":
        q="select * from employee"
        cur.execute(q)
        r = cur.fetchall()
        for i in r:
            print(*i,sep="  ")

    else:
        print("Invalid Operation")

    conn.commit()