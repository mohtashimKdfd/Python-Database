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
# s='CREATE TABLE student(studentID integer(4), name varchar(30),class integer(10), height float(5,2))'
#Already created Table
# s="INSERT INTO student (studentID,name,class,height) VALUES (%s,%s,%s,%s)"
# for _ in range(3):
#     sID = int(input('Enter the id of student:'))
#     naam = input('Enter the name of student:')
#     classs = int(input('Enter the class pf student'))
#     height  = input("Enter the height of student:")
#     st = (sID,naam,classs,height)

#     cur.execute(s,st)  #we can also pass arguments(objects that store our data to the execute command)

#     mydb.commit()   #commit function saves every changes made in our db

#     print('Added data into database')

#for inserting multiple records we can also create a list of tuples and pass that list into the excute function alongside the main string    

#Fetching values or data from database
# s="SELECT * from student"

# cur.execute(s)
# result = cur.fetchall()
# for res in result:
#     print(res)


# t="SELECT * from student WHERE height>5"
# cur.execute(t)Learn
# result = cur.fetchall()
# for res in result:
#     print(res)

# s="DELETE FROM student WHERE name='mk'"
# cur.execute(s)
# mydb.commit()

# Creating new table 
# s="CREATE TABLE teacher(teacherID integer(10), name varchar(30), subject varchar(20), salary integer(10))"

# data = [(1,'Mohtashim','Maths',10000),(2,'Pratyush','Physics',11000),(3,'Shivansh','Designing',9000),(4,'Sahil','Cashier',0),(5,'Tushar','HomeScience',2000)]
# s="INSERT INTO teacher(teacherID,name,subject,salary) VALUES (%s,%s,%s,%s)"
# cur.executemany(s,data)
# mydb.commit()

s="UPDATE teacher SET salary = salary+4000 where salary=0"

cur.execute(s)
mydb.commit()

print("Done")
