import sqlite3
import sys
from datetime import date

def giveVote(uid, c):
    pid_tar = input("Put the post ID that you want to vote: ")
    c.execute('''SELECT * FROM posts p WHERE p.pid = (:pid);''', {"pid": pid_tar})
    row = c.fetchone()
    if row == []:
        print("the post id does not exist, going back to menu...")
        return
    c.execute('''SELECT * FROM votes v WHERE v.pid = :pid AND v.uid = :uid;''', {"pid": pid_tar, "uid":uid})
    row = c.fetchone()
    if row is not None:
        print("you already voted for this posts, going back to menu...")
        return
    c.execute('''SELECT v.vno FROM votes v ORDER BY vno DESC LIMIT 1;''')
    row = c.fetchone()
    vnoOld = row[0]
    vnoNew = vnoOld + 1
    print(vnoNew)
    c.execute("INSERT INTO votes VALUES(:pid ,:vno , :vdate , :uid)",
                {"pid":pid_tar, "vno":vnoNew,"vdate":date.today(), "uid":uid})

def func_test():
    conn = sqlite3.connect('./assignment.db')	
    c = conn.cursor()
    giveVote("mldang", c)