import sqlite3
from datetime import date
def privUserEdit(conn,pid):
    c	=	conn.cursor()
    print("\r\n------------------------------------------------Edit Page------------------------------------------------\r\n")
    query = "Select * from posts p1 Where p1.pid = \""+ pid+"\";"
    c.execute(query)
    rowEdit = c.fetchall()
    rowEdit = rowEdit[0]
    print("Current row your editing:")
    print("PID:    " + str(rowEdit[0]))
    print("Title:  " + rowEdit[2])
    print("Body:   " + rowEdit[3])
    title = input("Please input a new title:  ")
    body = input ("Please enter a new body   ")
    c.execute('''UPDATE 'posts' SET title = (:title) , body = (:body) WHERE pid = (:pid);''',
              {"title":title, "body":body, "pid":rowEdit[0]})
    conn.commit()
    print("Success!")
    print("\r\n--------------------------------------------------------------------------------------------------------\r\n")