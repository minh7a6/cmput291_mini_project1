from login import loginPage
import sqlite3
from main_menu import main_menu 
def main():
    conn	=	sqlite3.connect('./test_data.db')	
    uid = loginPage(conn)
    main_menu(uid,conn)
if __name__ == "__main__":
    main()