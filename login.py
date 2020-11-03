from datetime import date

import sqlite3
import sys
import re

def loginPage(conn):
    print("\r\n------------------------------------------------Login Page------------------------------------------------")
    pattern = re.compile("")
    c = conn.cursor()
    print("1. Login")
    print("2. Sign up") 	
    LogSignOption = input("Please press 1 or 2 for which option you would like to pick: ")
    tryAgain = True
    userId = 0
    if LogSignOption == "1":
        while(tryAgain):
            print("Login page")
            userId = input("Please enter your user id: ")
            password = input ("Please enter your password: ")
            c.execute('''Select uid FROM users WHERE uid= :userId AND pwd = :password;''',
                    {"userId": userId, "password":password})
            rows = c.fetchall()
            if(rows!=[]):
                print("Success!")
                tryAgain = False
                return userId
            else:
                tryAgain = input("Wrong Username or password. Would you like to try again(1: Yes) (2: No)?  " )
                if tryAgain == "2":
                    conn.close()
                    sys.exit("leaving....")
        return userId
    elif LogSignOption=="2":
        print ("Sign Up page")
        newUserId = input("Please enter a user id: ")
        c.execute('Select uid FROM users WHERE uid=?;', (newUserId,))
        rows = c.fetchone()
        while rows !=[] or len(newUserId) > 4 or (not newUserId.isalnum()):
            if len(newUserId) > 4:
                key = input("User ID can only have maximum of 4 letters. Do you want to try another(1: yes)? ")
            elif not newUserId.isalnum():
                key = input("User ID can only have alphanumeric letter Do you want to try another(1: yes)? ")
            else:
                key = input("You have entered in a duplicate user Id. Do you want to try another(1: yes)? ")
            if key == "1":
                newUserId = input("Please enter a user id: ")
                c.execute('Select uid FROM users WHERE uid=?;', (newUserId,))
                rows = c.fetchone()
            else:
                conn.close()
                sys.exit("leaving....")
        newName = input ("Please enter your name: ")
        newPassword = input ("Please enter your password: ")
        while not newPassword.isalnum():
            newPassword = input("Password can only contain alphanumeric character. Please try again: ")
        newCity = input ("Please enter your city: ")
        c.execute('''INSERT INTO users VALUES(:userId ,:name , :pwd , :city , :crdate );''',
                {"userId":newUserId, "name":newName,"pwd":newPassword, "city":newCity, "crdate":date.today()})
        conn.commit()
        print("Success!")
        return newUserId
    else:
        conn.close()
        sys.exit("Wrong Option, exiting out of program")
