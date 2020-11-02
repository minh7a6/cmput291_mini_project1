import sqlite3
import sys
from datetime import date
from uuid import uuid4

def giveVote(uid, conn, pid_tar):
    c = conn.cursor()
    # pid_tar = input("Put the post ID that you want to vote: ")
    # c.execute('''SELECT * FROM posts p WHERE p.pid = (:pid);''', {"pid": pid_tar})
    # row = c.fetchone()
    # if row is None:
    #     print("the post id does not exist, going back to menu...")
    #     return
    c.execute('''SELECT * FROM votes v WHERE v.pid = :pid AND v.uid = :uid;''', {"pid": pid_tar, "uid":uid})
    row = c.fetchone()
    if row is not None:
        print("you already voted for this posts, going back to menu...")
        return
    vnoNew = str(uuid4().int)
    c.execute('''SELECT v.vno FROM votes v WHERE v.pid = (:pid) AND v.vno = (:vno);''', {"pid":pid_tar, "vno":vnoNew})
    row = c.fetchone()
    while row is not None:
        vnoNew = str(uuid4().int)
        c.execute('''SELECT v.vno FROM votes v WHERE v.pid = (:pid) AND v.vno = (:vno);''', {"pid":pid_tar, "vno":vnoNew})
        row = c.fetchone()
    c.execute('''INSERT INTO 'votes' VALUES(:pid ,:vno , :vdate , :uid);''',
                {"pid":pid_tar, "vno":vnoNew,"vdate":date.today(), "uid":uid})
    conn.commit()

def func_test():
    conn = sqlite3.connect('./test_data.db')
    giveVote("mldang", conn, "p048")
# func_test()