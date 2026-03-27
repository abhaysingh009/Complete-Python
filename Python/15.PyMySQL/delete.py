import pymysql as sq
con=sq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor=con.cursor();
x=mycursor.execute("Delete from student where st_id=3")
if x>0:
    print("deleted")
else:
    print("failed")
con.commit()
con.close()