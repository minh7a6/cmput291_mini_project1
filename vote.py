import sqlite3
import sys
from datetime import date
from util import numGen

"""
Function: giveVote(uid, conn, pid_tar)
Description: this is to give a vote for a post no matter if it is a question or an answer. This function is avaialable for
            normal/privileged user
"""

def giveVote(uid, conn, pid_tar):
    print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
    c = conn.cursor()
    c.execute('''SELECT * FROM votes v WHERE v.pid = :pid AND v.uid = :uid;''', {"pid": pid_tar, "uid":uid})
    row = c.fetchone()
    if row is not None:
        print("You already voted for this posts")
        print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
        return
    print("Starting to Vote...")
    vnoNew = numGen(4)
    c.execute('''SELECT v.vno FROM votes v WHERE v.pid = (:pid) AND v.vno = (:vno);''', {"pid":pid_tar, "vno":vnoNew})
    row = c.fetchone()
    while row is not None:
        vnoNew = numGen(4)
        c.execute('''SELECT v.vno FROM votes v WHERE v.pid = (:pid) AND v.vno = (:vno);''', {"pid":pid_tar, "vno":vnoNew})
        row = c.fetchone()
    c.execute('''INSERT INTO 'votes' VALUES(:pid ,:vno , :vdate , :uid);''',
                {"pid":pid_tar, "vno":vnoNew,"vdate":date.today(), "uid":uid})
    conn.commit()
    print("Success!")
    print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
def func_test():
    conn = sqlite3.connect('./test_data.db')
    giveVote("mldang", conn, "p048")
# func_test()