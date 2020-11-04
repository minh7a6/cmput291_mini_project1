import sqlite3
from datetime import date

"""
Function: giveTag(uid, conn, pid)
Description: this is to give a tag to the post (pid), this function is only available for privileged user.
"""
def giveTag(uid, conn, pid):
    c = conn.cursor()
    print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
    tag = input("What tag would you like to give? ")
    script = "SELECT t.tag FROM tags t WHERE t.pid = '" + str(pid) + "' AND LOWER(t.tag) = LOWER('" + str(tag) +"');"
    c.execute(script)
    row = c.fetchone()
    if row is not None:
        print("Duplicate tag")
        print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
        return
    c.execute('''INSERT INTO 'tags' VALUES(:pid, :tag);''',{"pid": pid, "tag": tag})
    conn.commit()
    print("Success!")
    print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
def func_test():
    conn = sqlite3.connect('./test_data.db')	
    giveTag("mldang", conn, "p005")
# func_test()