#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[4]:


db=sqlite3.connect("Sports_database.db")


# In[5]:


cur=db.cursor()


# In[6]:


cur.execute("create table sport(id int primary key, sport name text unique, dateofevent, country text not null)")


# In[12]:


cur.execute("insert into sport values(101, 'Cricket','2022-05-01', 'India' )")


# In[13]:


cur.execute("insert into sport values(102, 'Football','2022-05-02', 'Srilanka' )")


# In[14]:


cur.execute("insert into sport values(104, 'Volleyball','2022-05-03', 'London' )")


# In[15]:


cur.execute("insert into sport values(105, 'Hockey','2022-05-04', 'USA' )")


# In[16]:


cur.execute("insert into sport values(107, 'Tennis','2022-05-05', 'Maldives' )")


# In[33]:


results=cur.execute("select * from sport")
results.fetchall()


# # Employee database with DB and Python Programm

# In[37]:


import sqlite3


# In[39]:


con=sqlite3.connect('Employee_database.db')


# In[74]:


def sql_table(con):
    cur=con.cursor()
    cur.execute("create table employee(id integer primary key, name text, salary real, department text)")
    con.commit()


# In[62]:


#calling function
sql_table(con)


# In[84]:


cur=con.cursor()
cur.execute("insert into employee values(12,'Jack',2500,'HR')")


# In[89]:


results=cur.execute("select * from employee")
results.fetchall()


# In[118]:


def sql_insert(con,entities):
    cr=con.cursor()
    cur.execute("insert into employee(id,name, salary, department) values(?,?,?,?)",entities)


# In[119]:


entities=(1,'Sam',1500,'Finance')


# In[124]:


results=cur.execute("select * from employee")
results.fetchall()


# In[133]:


def sql_query(sql):
    cur=con.cursor()
    results=cur.execute(sql)
    return results


# In[134]:


sql="select * from employee"
respond=sql_query(sql)
respond.fetchall()


# In[135]:


#cur.executemany is used to insert multiple rows in a data base


# # Referential Integrity

# In[136]:


import sqlite3


# In[137]:


db=sqlite3.connect("Student_course_database.db")


# In[138]:


cur=db.cursor()


# In[143]:


cur.execute("create table course(courseid int primary key, coursename text, duration int)")


# In[146]:


cur.execute("create table student(roll_no int primary key, name text, age int, courseid int, foreign key(courseid) references course(courseid))")


# In[147]:


cur.execute("insert into course values(101, 'Data Science', 12),(112,'Python',4),(103,'Tabelue',3)")


# In[148]:


print(cur.rowcount,'Records inserted')


# In[149]:


cur.execute("insert into student values(1,'Jack',22,101),(2,'Sam',33,101),(3,'Sean',23,112)")
print(cur.rowcount,'Records inserted')


# In[150]:


results=cur.execute('select * from student')
results.fetchall()

