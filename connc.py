import mysql.connector as my
conn=my.connect(user='root',password='root',host='localhost', database='ind')
cur=conn.cursor()
# q="create database ind"
# q="show databases"
# q="create table stud(name varchar(20),roll int,class varchar(10))"
# q="insert into stud values('inder',1,'fy')"
# q="insert into stud values('harshal',2,'sy')"
# q="insert into stud values('akshay',3,'ty')"
#

# n=input("enter name:")
# r=int(input("enter roll_no:"))
# c=input("enter class")
# v=(n,r,c)
# q="insert into stud (name,roll,class ) values(%s,%s,%s)"
# cur.execute(q,v)

# q= "insert into stud(name,roll,class) values (%s,%s,%s)"
# v=[
# ('siddhesh',6,'sy'),
# ('sid',7,'fy'),
# ('shubham',8,'ty')
# ]

# n=input("enter name:")
# r=int(input("enter roll_no:"))
# v=(n,r)
# q="update stud set name=%s where roll=%s"
# cur.execute(q,v)
n=input("enter name:")
q=("delete from stud where name='%s'")%(n)
cur.execute(q)
conn.commit()





