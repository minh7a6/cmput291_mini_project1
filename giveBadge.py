import sqlite3
from datetime import date

def giveBadge(uid, conn):
    c = conn.cursor()
    uid = input("Put the uid you would like to give badge today: ")
    c.execute('''SELECT u.uid FROM users u WHERE u.uid = (:uid)''', {"uid": uid})
    row = c.fetchone()
    if row is None:
        print("The uid does not exist in database, going back to menu...")
        return
    bname = input("What badge would you like to give today?: ")
    c.execute('''SELECT * FROM badges WHERE bname = (:bname)''', {"bname": bname})
    row = c.fetchone()
    if row is None:
        print("The badge name does not exist in database, going back to menu...")
        return
    c.execute('''INSERT INTO 'ubadges' VALUES(:uid, :bdate, :bname);''',{"uid": uid, "bname": bname, "bdate": date.today()})
    conn.commit()

def func_test():
    conn = sqlite3.connect('./test_data.db')	
    giveBadge("mldang", conn)
# func_test()