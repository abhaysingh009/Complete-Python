import pymysql as sq

con=sq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycursor=con.cursor()

# Cursor = tool to execute SQL queries

# 🔹 Internally:
# Cursor acts like a bridge
# It sends queries to DB and receives results

try:
    ins="INSERT INTO STUDENT(st_name,st_email) VALUES (%s,%s)"
    mycursor.execute(ins,('Aman','aman@gmail.com'))
    con.commit() #used always when we do manipulation in table

except Exception:
    print("Error")

