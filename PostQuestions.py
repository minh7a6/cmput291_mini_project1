import sqlite3
from datetime import date
from numGen import numGen
def Post(uid,conn):
    c = conn.cursor()
    print("\r\n------------------------------------------------Post Page------------------------------------------------")
    title = input("PLease input a title: ")
    body =  input("Please input the body:  ")
    pidNew = numGen(4)
    c.execute('''SELECT pid FROM posts WHERE pid = (:pid);''', {"pid": pidNew})
    row = c.fetchone()
    while row is not None:
        pidNew = numGen(4)
        c.execute('''SELECT pid FROM posts WHERE pid = (:pid);''', {"pid": pidNew})
        row = c.fetchone()
    c.execute('''INSERT INTO posts VALUES(:pid ,:date , :title , :body , :uid );''',
              {"pid":pidNew, "date":date.today(),"title":title, "body":body, "uid":uid})
    c.execute('''INSERT INTO questions(pid) VALUES(:pid);''', {"pid": pidNew})
    conn.commit()
    print("Success!")
    print("\r\n--------------------------------------------------------------------------------------------------------\r\n")