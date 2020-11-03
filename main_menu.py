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
#Function normal_menu
#Args : uid - uid of user using the program, conn - connection to database
#Desciption: provides menue for non Privileged  users
def normal_menu(uid, conn):
    c = conn.cursor()
    c.execute('''SELECT name FROM users WHERE uid = (:uid);''', {"uid": uid})
    row = c.fetchone()
    while True:
        print("Hello {0} ! What would you like to do today?".format(row[0]))
        print("1: Post a Question")
        print("2: Search for a Post")
        print("3: Post action-Answer")
        print("4: Post action-Vote")
        print("5: Exit")
        sel = input("Please choose an option: ")
        if sel == "1":
            Post(uid, conn)
        elif sel == "2":
            c = conn.cursor()
            SearchMain(c)
        elif sel == "3":
            giveAns(uid, conn)
        elif sel == "4":
            giveVote(uid, conn)
        elif sel == "5":
            print("Goodbye...")
            exit(conn)
            break
        else: 
            print("Invalid option")
#Function privileged_menu
#Args : uid - uid of user using the program, conn - connection to database
#Desciption: provides menue for  Privileged  users
def privileged_menu(uid, conn):
    c = conn.cursor()
    c.execute('''SELECT name FROM users WHERE uid = (:uid);''', {"uid": uid})
    row = c.fetchone()
    while True:
        print("Hello {0} ! What would you like to do today?".format(row[0]))
        print("1: Post a Question")
        print("2: Search for a Post")
        print("3: Post action-Answer")
        print("4: Post action-Vote")
        print("5: Post action-Mark as the accepted")
        print("6: Post action-Give a badge")
        print("7: Post action-Add a tag")
        print("8: Post Action-Edit")
        print("9: Exit")
        sel = input("Please choose an option: ")
        if sel == "1":
            Post(uid, conn)
        elif sel == "2":
            c = conn.cursor()
            SearchMain(c)
        elif sel == "3":
            giveAns(uid, conn)
        elif sel == "4":
            giveVote(uid, conn)
        elif sel == "5":
            acceptedAns(uid, conn)
        elif sel == "6":
            giveBadge(uid, conn)
        elif sel == "7":
            giveTag(uid, conn)
        elif sel =="8":
            privUserEdit(conn,pid)
        elif sel == "9":
            print("Goodbye...")
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
