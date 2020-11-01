import sqlite3
from datetime import date

def giveTag(uid, conn):
    c = conn.cursor()
    pid = input("Put the post you would like to give tag: ")
    c.execute('''SELECT pid FROM posts WHERE pid = (:pid);''', {"pid": pid})
    row = c.fetchone()
    if row is None:
        print("Post ID does not exist in database, going back to menu...")
        return
    tag = input("What tag would you like to give? ")
    c.execute('''SELECT t.tag FROM tags t WHERE t.pid = (:pid) AND INSTR(LOWER(t.tag), LOWER(:tag)) > 0;''', {"pid": pid, "tag": tag})
    row = c.fetchone()
    if row is not None:
        print("tag already exists for that posts, going back to menu...")
        return
    c.execute('''INSERT INTO 'tags' VALUES(:pid, :tag);''',{"pid": pid, "tag": tag})
    conn.commit()

def func_test():
    conn = sqlite3.connect('./test_data.db')	
    giveTag("mldang", conn)
# func_test()