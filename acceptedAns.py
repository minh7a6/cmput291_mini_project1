import sqlite3
import sys
from datetime import date

def acceptedAns(uid, conn):
    c = conn.cursor()
    pid_input = input("Put the post ID that you want to accept as answer: ")
    c.execute('''SELECT a.qid FROM answers a WHERE a.pid = (:pid);''', {"pid": pid_input})
    row = c.fetchone()
    if row is None:
        print("The post id is not in the answer, going back to menu...")
        return
    q_pid = row[0]
    c.execute('''SELECT * FROM questions q WHERE q.pid = (:pid);''', {"pid": q_pid})
    row = c.fetchall()
    if len(row) > 1:
        sel = input("The question already has an accepted answer, do you still want to continue (1: yes) (2: no)? ")
        if sel == "2":
            print("Going back to menu...")
            return
    c.execute('''UPDATE 'questions' SET theaid = (:theaid) WHERE pid = (:pid)''', {"pid":q_pid, "theaid": pid_input})
    conn.commit()

def func_test():
    conn = sqlite3.connect('./test_data.db')
    acceptedAns("mldang", conn)
func_test()