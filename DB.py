##ELECTRONIC SHOP MANAGEMENT SYSTEM##
##DB.py##
import mysql.connector as b
c=b.connect(host='localhost',user='root',passwd='admin')
d=c.cursor()
d.execute('create database ESMS;')
d.execute('create database BILLS;')
print('Database creation successful')
