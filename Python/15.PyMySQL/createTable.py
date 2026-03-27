import pymysql as mq
con=mq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mysqlc=con.cursor()

tc='''
create table Student (
        st_id INT PRIMARY KEY AUTO_INCREMENT,
        st_name varchar(40),
        st_email varchar(50)
)'''

mysqlc.execute(tc)
