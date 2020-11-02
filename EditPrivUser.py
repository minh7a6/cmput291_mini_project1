import sqlite3
from datetime import date
def privUserEdit(conn):
    c	=	conn.cursor()
    print("\r\n------------------------------------------------Edit Page------------------------------------------------")
    print("\r\n------------------------------------------------Current posts----------------------------------------------")
    c.execute("""Select p1.pid, p1.title, p1.body
                  from posts p1""")
    table = c.fetchall()
    print("PID || Title || Body")
    print("\r\n----------------------------------------------------------------------------------------------")
    for x in table:
        print(x[0] +" ||  "+x[1]+" ||  "+x[2])        
    print("\r\n----------------------------------------------------------------------------------------------")
    pidEdit = input ("Please enter a PID that you would like to edit  ")
    query = "Select * from posts p1 Where p1.pid = \""+ pidEdit+"\";"
    c.execute(query)
    retry = False
    rowEdit = c.fetchall()
    if(rowEdit==[]):
        retry = True
    while(retry):
        pidEdit = input("You have entered a PID that does not exist please try again  ")
        query = "Select * from posts p1 Where p1.pid = \""+ pidEdit+"\";"
        c.execute(query)
        rowEdit = c.fetchall()
        if(rowEdit!=[]):
            retry = False
    rowEdit = rowEdit[0]
    print("Current row your editing:")
    print("PID:    " + str(rowEdit[0]))
    print("Title:  " + rowEdit[2])
    print("Body:   " + rowEdit[3])
    title = input("Please input a new title:  ")
    body = input ("Please enter a new body   ")
    c.execute('''UPDATE 'posts' SET title = (:title) , body = (:body) WHERE pid = (:pid);''',
              {"title":title, "body":body, "pid":rowEdit[0]})