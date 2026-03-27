import sqlite3
con=sqlite3.connect("Abhay.db")

con.execute('''
update Student set st_name='Ram' where st_id=1

''')
con.commit()
con.close()