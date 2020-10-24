# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sqlite3
conn	=	sqlite3.connect('./assigment.db')	
c	=	conn.cursor()
def createTable():
    c.executescript('''drop table if exists answers;
    drop table if exists questions;
    drop table if exists votes;
    drop table if exists tags;
    drop table if exists posts;
    drop table if exists ubadges;
    drop table if exists badges;
    drop table if exists privileged;
    drop table if exists users;
    
    PRAGMA foreign_keys = ON;
    
    create table users (
      uid		char(4),
      name		text,
      pwd		text,
      city		text,
      crdate	date,
      primary key (uid)
    );
    create table privileged (
      uid		char(4),
      primary key (uid),
      foreign key (uid) references users
    );
    create table badges (
      bname		text,
      type		text,
      primary key (bname)
    );
    create table ubadges (
      uid		char(4),
      bdate		date,
      bname		text,
      primary key (uid,bdate),
      foreign key (uid) references users,
      foreign key (bname) references badges
    );
    create table posts (
      pid		char(4),
      pdate		date,
      title		text,
      body		text,
      poster	char(4),
      primary key (pid),
      foreign key (poster) references users
    );
    create table tags (
      pid		char(4),
      tag		text,
      primary key (pid,tag),
      foreign key (pid) references posts
    );
    create table votes (
      pid		char(4),
      vno		int,
      vdate		text,
      uid		char(4),
      primary key (pid,vno),
      foreign key (pid) references posts,
      foreign key (uid) references users
    );
    create table questions (
      pid		char(4),
      theaid	char(4),
      primary key (pid),
      foreign key (theaid) references answers
    );
    create table answers (
      pid		char(4),
      qid		char(4),
      primary key (pid),
      foreign key (qid) references questions
    );''')
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
             
createTable()
loginPage()

