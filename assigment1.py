# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sqlite3
conn	=	sqlite3.connect('./assigment.db')	
c	=	conn.cursor()
def loginPage():
      print("1. Login")
      print("2. Sign up") 	
      LogSignOption = input("Please press 1 or 2 for which option you would like to pick: ")
      if LogSignOption == "1":
          print("Login page")
          userId = input("Please enter your user id")
          password = input ("Please enter your password")
      elif LogSignOption=="2":
          print ("Signup page")
          newUserId = input("Please enter a user id")
          newName = input ("Please enter your name")
          newPassword = input ("Please enter your password")
          newCity = input ("Please enter your city")
          unique = False;
          rows = c.fetchall()
          c.execute('Select uid FROM users WHERE uid=?;', newUserId)
          while(rows !=[]):
              print("You have entered in a duplicate user Id please try enter another")
              newUserId = input("Please enter a user id")
              newName = input ("Please enter your name")
              newPassword = input ("Please enter your password")
              newCity = input ("Please enter your city")
          
          c.execute('''INSERT INTO users VALUES(:userId ,:name , :pwd , :city , :crdate )''',
                    {"userId":newUserId, "name":newName,"pwd":newPassword, "city":newCity, "crdate":'12-07-2020'})
          c.execute('SELECT	*	FROM	users')
                  
          
 

         ''' rows = c.fetchall()
          print(rows)'''
loginPage()

