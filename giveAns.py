import sqlite3
from datetime import date
from sqlite3.dbapi2 import Date
from util import numGen

def giveAns(uid, conn, pid):
    print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
    c = conn.cursor()
    c.execute('''SELECT q.pid FROM questions q WHERE q.pid = :pid;''', {"pid": pid})
    row = c.fetchone()
    if row is None:
        print("The post id is not a question")
        print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
        return
    pidNew = numGen(4)
    c.execute('''SELECT pid FROM posts WHERE pid = (:pid);''', {"pid": pidNew})
    row = c.fetchone()
    while row is not None:
        pidNew = numGen(4)
        c.execute('''SELECT pid FROM posts WHERE pid = (:pid);''', {"pid": pidNew})
        row = c.fetchone()
    title = input("What is your title for this answer: ")
    body = input("Put the Content of your answers here: ")
    c.execute('''INSERT INTO 'posts' VALUES(:pid ,:pdate , :title , :body, :poster);''',
                {"pid": pidNew, "pdate": date.today(), "title": title, "body":body, "poster": uid})
    c.execute('''INSERT INTO 'answers' VALUES(:pid, :qid);''', {"pid": pidNew, "qid": pid})
    conn.commit()
    print("Success!")
    print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
def func_test():
    conn = sqlite3.connect('./test_data.db')	
    giveAns("mldang", conn)
# func_test()