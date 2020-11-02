import sqlite3

from giveAns import giveAns
from vote import giveVote
from acceptedAns import acceptedAns
from giveBadge import giveBadge
from giveTag import giveTag
from PostQuestions import Post
from SearchPost import SearchMain
from EditPrivUser import privUserEdit


def exit(conn):
    conn.close()

def normal_menu(uid, conn):
    c = conn.cursor()
    c.execute('''SELECT name FROM users WHERE uid = (:uid);''', {"uid": uid})
    row = c.fetchone()
    while True:
        print("Hello {0} ! What would you like to do today?".format(row[0]))
        print("1: Post a Question")
        print("2: Search for a Post")
        print("3: Log Out")
        sel = input("Please choose an option: ")
        if sel == "1":
            Post(uid, conn)
        elif sel == "2":
            table = SearchMain(conn.cursor())
            if len(table) > 0:
                while True:
                    print("What would you like to do with the post? ")
                    print("1: Post action-Answer")
                    print("2: Post action-Vote")
                    print("3: Exit")
                    sel = input("Please choose an option: ")
                    if sel == "1":
                        giveAns(uid, conn, table[0])
                    elif sel == "2":
                        giveVote(uid, conn, table[0])
                    elif sel == "3":
                        print("Going back to menu")
                        exit(conn)
                        break
                    else: 
                        print("Invalid option")
        elif sel == "3":
            print("Logging out...")
            exit(conn)
            break
        else: 
            print("Invalid option")

def privileged_menu(uid, conn):
    c = conn.cursor()
    c.execute('''SELECT name FROM users WHERE uid = (:uid);''', {"uid": uid})
    row = c.fetchone()
    while True:
        print("Hello {0} ! What would you like to do today?".format(row[0]))
        print("1: Post a Question")
        print("2: Search for a Post")
        print("3: Log Out")
        sel = input("Please choose an option: ")
        if sel == "1":
            Post(uid, conn)
        elif sel == "2":
            table = SearchMain(conn.cursor())
            if len(table) > 0:
                while True:
                    print("What would you like to do with the post? ")
                    print("1: Post action-Answer")
                    print("2: Post action-Vote")
                    print("3: Post action-Mark as the accepted")
                    print("4: Post action-Give a badge")
                    print("5: Post action-Add a tag")
                    print("6: Post Action-Edit")
                    print("7: Exit")
                    sel = input("Please choose an option: ")
                    if sel == "1":
                        giveAns(uid, conn, table[0])
                    elif sel == "2":
                        giveVote(uid, conn, table[0])
                    elif sel == "3":
                        acceptedAns(uid, conn, table[0])
                    elif sel == "4":
                        giveBadge(uid, conn, table[1])
                    elif sel == "5":
                        giveTag(uid, conn, table[0])
                    elif sel =="6":
                        privUserEdit(conn, table[0])
                    elif sel == "7":
                        print("Going back to menu")
                        exit(conn)
                        break
                    else: 
                        print("Invalid option")
        elif sel == "3":
            print("Logging out...")
            exit(conn)
            break
        else: 
            print("Invalid option")

def main_menu(uid, conn):
    c = conn.cursor()
    print("\r\n------------------------------------------------Main Menu------------------------------------------------")
    c.execute('''SELECT * FROM privileged WHERE uid = (:uid);''', {"uid": uid})
    row = c.fetchone()
    if row is None:
        normal_menu(uid, conn)
    else: 
        privileged_menu(uid, conn)

# def func_test():
#     conn = sqlite3.connect('./test_data.db')	
#     main_menu("mldang", conn)
# func_test()
