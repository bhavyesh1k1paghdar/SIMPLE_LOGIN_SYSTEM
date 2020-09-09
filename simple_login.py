import sqlite3 

db=sqlite3.connect("simple_login.db")
cr=db.cursor()
cr.execute("create table login(UNAME text,UPASS text)")
db.commit()
db.close()
  
