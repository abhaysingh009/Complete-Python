import sqlite3
con=sqlite3.connect("Abhay.db")

# dele='''
# DELETE FROM STUDENT WHERE st_id=2
# '''
con.execute("drop table student")
con.commit()
con.close() 