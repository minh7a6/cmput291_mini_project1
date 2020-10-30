from login import loginPage
import sqlite3
import sys
from main_menu import menu 
def main():
    conn	=	sqlite3.connect('./assignment.db')	
    c	=	conn.cursor()
    uid = loginPage(c)
    menu(uid,c)
    
if __name__ == "__main__":
    main()