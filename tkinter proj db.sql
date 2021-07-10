create database inder;
use inder;
create table regdb(
id int primary key auto_increment, 
username varchar (30), 
password varchar (30), 
contact bigint,
email varchar (30));


create table forms( 
id int primary key auto_increment, 
fname varchar (30), 
lname varchar (30), 
contact bigint,
email varchar(30), 
gender varchar (7),
hobby varchar (40),
qualification varchar (20), 
age int,
address varchar (400));


id            | int          | NO   | PRI | NULL    | auto_increment |
| fname         | varchar(30)  | YES  |     | NULL    |                |
| lname         | varchar(30)  | YES  |     | NULL    |                |
| contact       | bigint       | YES  |     | NULL    |                |
| email         | varchar(30)  | YES  |     | NULL    |                |
| gender        | varchar(7)   | YES  |     | NULL    |                |
| hobby         | varchar(40)  | YES  |     | NULL    |                |
| qualification | varchar(20)  | YES  |     | NULL    |                |
| age           | int          | YES  |     | NULL    |                |
| address       | varchar(400)