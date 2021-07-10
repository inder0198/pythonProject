import mysql.connector as my
conn=my.connect(user='root',password='root',host='localhost',database='ashraful')
cur=conn.cursor()
#q="create database ashraful"
#q="create table stud(name varchar(20),roll int,class varchar(10))"
#q="insert into stud values('xyz',2,'TY')"
# q="select * from stud"
# cur.execute(q)
# r=cur.fetchall()
# for i in r:
#     print(i)
n=input("enter name:")
# r=int(input("enter roll_no:"))
# # c=input("enter class")
# # v=(n,r,c)
# # q="insert into stud (name,roll,class ) values(%s,%s,%s)"
# # cur.execute(q,v)
# # conn.commit()
# v=(n,r)
# q="update stud set name=%s where roll=%s"
# cur.execute(q,v)
# conn.commit()
q=("delete from stud where name='%s'")%(n)
cur.execute(q)
conn.commit()