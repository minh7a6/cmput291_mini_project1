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
                print("Sucess")
                tryAgain = False
                return userId
            else:
                tryAgain = input("Wrong Username or password. Would you like to try again(1: Yes) (2: No)?  " )
                if tryAgain == "2":
                    conn.close()
                    sys.exit("leaving....")
        return userId
    elif LogSignOption=="2":
        print ("Signup page")
        newUserId = input("Please enter a user id: ")
        while len(newUserId) > 4:
            newUserId = input("UID exceeds 4 characters. Please try again: ")
        c.execute('Select uid FROM users WHERE uid=?;', (newUserId,))
        rows = c.fetchall()
        while(rows !=[]):
            key = input("You have entered in a duplicate user Id do you want to try another(1: yes) (2:no)? ")
            if key == "1":
                newUserId = input("Please enter a user id ")
                c.execute('Select uid FROM users WHERE uid=?;', (newUserId,))
                rows = c.fetchall()
            else:
                conn.close()
                sys.exit("leaving....")
        newName = input ("Please enter your name: ")
        newPassword = input ("Please enter your password: ")
        newCity = input ("Please enter your city: ")
        c.execute('''INSERT INTO users VALUES(:userId ,:name , :pwd , :city , :crdate );''',
                {"userId":newUserId, "name":newName,"pwd":newPassword, "city":newCity, "crdate":date.today()})
        conn.commit()
        print("Success!")
        return newUserId
    else:
        conn.close()
        sys.exit("Wrong Option, exiting out of program")
