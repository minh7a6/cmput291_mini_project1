from datetime import date

import sqlite3
import sys
import re
#Function loginPage
#Args :conn -connection to database
#Desciption: Provides the login page where users can signup or sign in
def loginPage(conn):
    while True:
        print("\r\n------------------------------------------------Login Page------------------------------------------------")
        c = conn.cursor()
        print("1. Login")
        print("2. Sign up") 
        print("3: Exit")	
        LogSignOption = input("Please choose an option: ")
        userId = 0
        if LogSignOption == "1":
            print("Login page")
            userId = input("Please enter your user id: ")
            password = input ("Please enter your password: ")
            c.execute('''Select uid FROM users WHERE uid= :userId AND pwd = :password;''',
                    {"userId": userId, "password":password})
            rows = c.fetchall()
            if(rows!=[]):
                print("Success!")
                return userId
            else:
                return print("User ID or password is not correct")
        elif LogSignOption=="2":
            print ("Sign Up Page")
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
                    return
            newName = input("Please enter your name: ")
            newPassword = input("Please enter your password: ")
            while not newPassword.isalnum():
                sel = input("Password can only contain alphanumeric character. Do you want to try another(1: yes)? ")
                if sel == "1":
                    newPassword = input("Please enter your password: ")
                else:
                    return
            newCity = input ("Please enter your city: ")
            c.execute('''INSERT INTO users VALUES(:userId ,:name , :pwd , :city , :crdate );''',
                    {"userId":newUserId, "name":newName,"pwd":newPassword, "city":newCity, "crdate":date.today()})
            conn.commit()
            print("Success!")
            return newUserId
        elif LogSignOption == "3":
            conn.close()
            sys.exit("Exiting...")
