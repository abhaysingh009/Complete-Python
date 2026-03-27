import pymysql as sq

con=sq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor=con.cursor();
mycursor.execute("select * from student")

try:
   myresult= mycursor.fetchall()
   for i in myresult:
      print(i)

except Exception:
   print ("error")