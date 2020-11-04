import sqlite3
from datetime import date

"""
Function: giveBadge(uid, conn, posters)
Description: this is to give a badge to the posters, this function is only available for privileged user.
"""

def giveBadge(uid, conn, posters):
    print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
    c = conn.cursor()
    c.execute('''SELECT * FROM ubadges WHERE bdate = (:bdate) AND uid = (:uid);''', {"bdate": date.today(), "uid":posters})
    row = c.fetchone()
    if row is not None:
        return print("This poster has received a badge today")
    bname = input("What badge would you like to give to {0} today?: ".format(posters))
    c.execute('''SELECT bname FROM badges WHERE LOWER(bname) = LOWER((:bname));''', {"bname": bname})
    row = c.fetchone()
    if row is None:
        print("The badge name does not exist in database")
        return

    c.execute('''INSERT INTO 'ubadges' VALUES(:uid, :bdate, :bname);''',{"uid": posters, "bname": row[0], "bdate": date.today()})
    conn.commit()
    print("Success!")
    print("\r\n--------------------------------------------------------------------------------------------------------\r\n")
def func_test():
    conn = sqlite3.connect('./test_data.db')	
    giveBadge("mldang", conn)
# func_test()