##ELECTRONICS SHOP MANAGEMENT SYSTEM##
##TABLE.py##
import mysql.connector as b
c=b.connect(host='localhost',user='root',passwd='admin')
d=c.cursor()
d.execute('use ESMS;')
d.execute('create table user(U_Name varchar(30),Password varchar(30), Name varchar(30),Ph_No bigint);')
d.execute('create table products(Prod_ID varchar(30),Prod_Name varchar(30),Quantity int,Price int);')
print('Table creation successful')

