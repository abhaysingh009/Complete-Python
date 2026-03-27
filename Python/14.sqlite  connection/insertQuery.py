import sqlite3
con=sqlite3.connect("Abhay.db")
ins='''
insert into student (st_name,st_email) values(?,?)   
'''
# insert into student (st_name,st_email) values('Aman','Aman@gmail.com') this is not prefered (Risk-> SQL injection)
con.execute(ins,('Rahul','Rahul@gmail.com'))
con.commit()  #Saves changes permanently to database   ,Without this, data may not be stored
con.close()