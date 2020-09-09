import sqlite3 

db=sqlite3.connect("simple_login.db")
cr=db.cursor()
cr.execute("create table register(NAME text,UNAME text,UEMAIL text,UPASS text,UCPASS text)")
db.commit()
db.close()
  
