import sqlite3
import sys
from datetime import date
from numGen import numGen

def giveVote(uid, conn, pid_tar):
    c = conn.cursor()
    c.execute('''SELECT * FROM votes v WHERE v.pid = :pid AND v.uid = :uid;''', {"pid": pid_tar, "uid":uid})
    row = c.fetchone()
    if row is not None:
        print("you already voted for this posts, going back to menu...")
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
def func_test():
    conn = sqlite3.connect('./test_data.db')
    giveVote("mldang", conn, "p048")
# func_test()