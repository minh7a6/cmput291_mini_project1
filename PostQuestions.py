import sqlite3
from datetime import date
#Function Post
#Args : uid - user id of the user posting question,conn -connection to database
#Desciption: post a question 
def Post(uid,conn):
    c = conn.cursor()
    print("\r\n------------------------------------------------Post Page------------------------------------------------")
    title = input("PLease input a title: ")
    body =  input("Please input the body:  ")
    c.execute('''SELECT PID FROM posts ORDER BY pid DESC LIMIT 1;''')
    pidOld = c.fetchall()[0][0]
    pidNew = "p"+str(int(pidOld[1:])+1)
    c.execute('''INSERT INTO posts VALUES(:pid ,:date , :title , :body , :uid )''',
              {"pid":pidNew, "date":date.today(),"title":title, "body":body, "uid":uid})
    # c.execute('''Select * from posts''')
    # print(c.fetchall())
    conn.commit()