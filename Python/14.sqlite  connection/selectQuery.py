import sqlite3
con=sqlite3.connect("Abhay.db")
x=0  #-->starting row 
y=5 #--> how many rows you want to select
sel=f'''
select * from student limit {x},{y}
'''

data=con.execute(sel)
# for i in data:
#     print(i)



print("Std id    Name     Gmail")
for i in data:
    print(i[0],"  \t",i[1],"\t  ",i[2])
con.close();