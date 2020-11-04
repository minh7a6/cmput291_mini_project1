import sqlite3
import sys
from datetime import date

"""
Function: acceptedAns(uid, conn, pid_input)
Description: this is to mark an answer is an accepted one for a question. This is only avalaible for the privileged user
"""

def acceptedAns(uid, conn, pid_input):
    print("\r\n--------------------------------------------------------------------------------------------------------")
    c = conn.cursor()
    # pid_input = input("Put the post ID that you want to accept as answer: ")
    c.execute('''SELECT a.qid FROM answers a WHERE a.pid = (:pid);''', {"pid": pid_input})
    row = c.fetchone()
    if row is None:
        print("The post id is not in the answer, going back to menu...")
        print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
        return
    q_pid = row[0]
    c.execute('''SELECT q.theaid FROM questions q WHERE q.pid = (:pid);''', {"pid": q_pid})
    row = c.fetchone()
    if row is not None:
        sel = input("The question already has an accepted answer, do you still want to continue (1: yes)? ")
        if sel == "1":
            print("Starting to change....")
        else: 
            return print("Wrong option")
    c.execute('''UPDATE 'questions' SET theaid = (:theaid) WHERE pid = (:pid)''', {"pid":q_pid, "theaid": pid_input})
    conn.commit()
    print("Success!")
    print("\r\n--------------------------------------------------------------------------------------------------------\r\n")

def func_test():
    conn = sqlite3.connect('./test_data.db')
    acceptedAns("mldang", conn)
# func_test()