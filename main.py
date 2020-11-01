from main_menu import func_test
from login import loginPage
import sqlite3
import sys
from main_menu import menu 
def main():
    conn	=	sqlite3.connect('./assignment.db')	
    uid = loginPage(conn)
    main_menu(uid,conn)
if __name__ == "__main__":
    main()