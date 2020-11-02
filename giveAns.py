import sqlite3
from datetime import date
from sqlite3.dbapi2 import Date

def giveAns(uid, conn, pid):
    c = conn.cursor()
    # pid = input("Put the post ID that you want to answer: ")
    c.execute('''SELECT q.pid FROM questions q WHERE q.pid = :pid;''', {"pid": pid})
    row = c.fetchone()
    if row is None:
        print("the post id is not a question, going back to menu...")
        return
    c.execute('''SELECT p.pid FROM posts p ORDER BY p.pid DESC LIMIT 1;''')
    row = c.fetchone()
    pidNew = "p" + str(int(row[0][1:]) + 1)
    title = input("What is your title for this answer: ")
    body = input("Put the Content of your answers here: ")
    c.execute('''INSERT INTO 'posts' VALUES(:pid ,:pdate , :title , :body, :poster);''',
                {"pid": pidNew, "pdate": date.today(), "title": title, "body":body, "poster": uid})
    c.execute('''INSERT INTO 'answers' VALUES(:pid, :qid);''', {"pid": pidNew, "qid": pid})
    conn.commit()
    
def func_test():
    conn = sqlite3.connect('./test_data.db')	
    giveAns("mldang", conn)
# func_test()