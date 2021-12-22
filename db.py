import mysql.connector
mydb= mysql.connector.connect(
    host='localhost',
    user='mohtashim@localhost',
    password='Ad_min',
    database='t1')

# print(mydb.connection_id)
#mydb will return connection object

# print(mydb.connection_id)
#cursor object is used to perform and execute any command in mysql
cur=mydb.cursor()
# print(cur)
#execute command is used to execute any query
# cur.execute("CREATE DATABASE t1")
s='CREATE TABLE student(studentID integer(4), name varchar(30),class integer(10), height float(5,2))'

cur.execute(s)
print("Done")