import sqlite3
import sys
from datetime import date

def giveVote(uid, c):
    pid_tar = input("Put the post ID that you want to vote: ")
    c.execute("SELECT * FROM posts p WHERE p.pid = ? ", pid_tar)
    row = c.fetchone()
    if(row == []):
        print("the post id does not exist, going back to menu...")
        return
    c.execute("SELECT * FROM votes v WHERE v.pid = ? AND v.uid = ?", pid_tar, uid)
    row = c.fetchone()
    if(row != []):
        print("you already voted for this posts, going back to menu...")
        return
    c.execute("SELECT v.vno FROM votes v ORDER BY vno DESC LIMIT 1;")
    vnoOld = c.fetchall()[0][0]
    vnoNew = "v"+str(int(vnoOld[1:])+1)
    c.execute("INSERT INTO votes VALUES(:pid ,:vno , :vdate , :uid)",
                {"pid":pid_tar, "vno":vnoNew,"vdate":date.today(), "uid":uid})