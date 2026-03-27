import pymysql as sq
try:
    with sq.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
    ) as con:
        mycursor=con.cursor()
        query="UPDATE STUDENT SET st_name=%s WHERE st_id=%s"
        x=mycursor.execute(query,('Aman',4))
        if x>0:
            con.commit()
            print("Updated successfully!")
        else:
            print("No record found!")
except Exception as e:
    print("Error: ",e)



# with sq.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="school"
#     ) as con:......    It is a standard way which reduces some manual work we can also use previous method for it