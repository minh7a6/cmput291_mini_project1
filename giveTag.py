import sqlite3
from datetime import date

def giveTag(uid, conn, pid):
    c = conn.cursor()
    print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
    tag = input("What tag would you like to give? ")
    keyword = tag.split(" ")
    script = "SELECT t.tag FROM tags t WHERE t.pid = '" + str(pid) + "' AND INSTR(LOWER(t.tag), LOWER('" + str(keyword[0]) +"')) > 0"
    for key in keyword:
        script += " UNION SELECT t.tag FROM tags t WHERE t.pid = '" + str(pid) + "' AND INSTR(LOWER(t.tag), LOWER('" + str(key) +"')) > 0"
    script += ";"
    c.execute(script)
    row = c.fetchone()
    if row is not None:
        print("To avoid duplicate, the tag name was there, please use other words")
        print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
        return
    c.execute('''INSERT INTO 'tags' VALUES(:pid, :tag);''',{"pid": pid, "tag": tag})
    conn.commit()
    print("Success!")
    print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
def func_test():
    conn = sqlite3.connect('./test_data.db')	
    giveTag("mldang", conn)
# func_test()