# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from datetime import date

import sqlite3
import sys

def loginPage(c):
    print("\r\n------------------------------------------------Login Page------------------------------------------------")
    print("1. Login")
    print("2. Sign up") 	
    LogSignOption = input("Please press 1 or 2 for which option you would like to pick: ")
    tryAgain = True
    if LogSignOption == "1":
        while(tryAgain):
            print("Login page")
            userId = input("Please enter your user id ")
            password = input ("Please enter your password ")
            c.execute('''Select uid FROM users WHERE uid= :userId AND pwd = :password;''',
                    {"userId": userId, "password":password})
            rows = c.fetchall()
            print(rows)
            if(rows!=[]):
                print("Sucess")
                return userId
            else:
                tryAgain = input("Wrong Username or password. Would you like to try again? Yes =1 No =2 " )
                if tryAgain == "2":
                    sys.exit("leaving....")
    elif LogSignOption=="2":
        print ("Signup page")
        newUserId = input("Please enter a user id ")
        c.execute('Select uid FROM users WHERE uid=?;', (newUserId,))
        rows = c.fetchall()
        while(rows !=[]):
            key = input("You have entered in a duplicate user Id do you want to try another(1: yes) (2:no)? ")
            if key == "1":
                newUserId = input("Please enter a user id ")
                c.execute('Select uid FROM users WHERE uid=?;', (newUserId,))
                rows = c.fetchall()
            else:
                sys.exit("leaving....")
        newName = input ("Please enter your name ")
        newPassword = input ("Please enter your password ")
        newCity = input ("Please enter your city ")
    #   while(rows !=[]):
    #       print("You have entered in a duplicate user Id please try enter another")
    #       newUserId = input("Please enter a user id ")
    #       newName = input ("Please enter your name ")
    #       newPassword = input ("Please enter your password ")
    #       newCity = input ("Please enter your city ")
    #       c.execute('Select uid FROM users WHERE uid=?;', (newUserId,))
    #       rows = c.fetchall()
        c.execute('''INSERT INTO users VALUES(:userId ,:name , :pwd , :city , :crdate )''',
                {"userId":newUserId, "name":newName,"pwd":newPassword, "city":newCity, "crdate":date.today()})
        c.execute('SELECT	*	FROM	users')
        return newUserId

