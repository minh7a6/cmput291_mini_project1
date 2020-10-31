from main_menu import func_test
from login import loginPage
import sqlite3
import sys
def main():
    conn	=	sqlite3.connect('./assignment.db')	
    c	=	conn.cursor()
    func_test(loginPage(c), c)

if __name__ == "__main__":
    main()