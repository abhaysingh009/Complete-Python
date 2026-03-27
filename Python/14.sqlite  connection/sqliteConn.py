import sqlite3
con=sqlite3.connect("Abhay.db")# connect with abhay.db if not exist then create
# execute --> to execute sqlite query
con.execute(''' 
create table Student(
            st_id INTEGER PRIMARY KEY AUTOINCREMENT,
            st_name varchar(20),
            st_email varchar(50)

             )
''')

#close the connection
con.close()
# --- DOWNLOAD DB BROWSER TO VIEW SQLITE TABLES -------------------