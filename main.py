from login import loginPage
import sqlite3
from main_menu import main_menu 
import sys
from os.path import isfile
def main(args):
    if not isfile(args) or not args.endswith('.db'):
        sys.exit("Unable to open database, please check your path and make sure database file has file type with '.db'.")
    conn	=	sqlite3.connect(args)	
    uid = loginPage(conn)
    main_menu(uid,conn)
if __name__ == "__main__":
    if(len(sys.argv) < 2):
        sys.exit("Please input your file")
    main(sys.argv[1])