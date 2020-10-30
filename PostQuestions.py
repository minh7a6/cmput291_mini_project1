import sqlite3
from datetime import date
def Post(uid,c):
    print("\r\n------------------------------------------------Post Page------------------------------------------------")
    title = input("PLease input a title: ")
    body =  input("Please input the body:  ")
    c.execute('''SELECT PID FROM posts ORDER BY pid DESC LIMIT 1;''')
    pidOld = c.fetchall()[0][0]
    pidNew = "p"+str(int(pidOld[1:])+1)
    c.execute('''INSERT INTO posts VALUES(:pid ,:date , :title , :body , :uid )''',
              {"pid":pidNew, "date":date.today(),"title":title, "body":body, "uid":uid})
    c.execute('''Select * from posts''')
    print(c.fetchall())
    