from login import loginPage
import sqlite3
import sys
def main():
    conn	=	sqlite3.connect('./assignment.db')	
    c	=	conn.cursor()
    while(1):
        print(loginPage(c))
if __name__ == "__main__":
    main()