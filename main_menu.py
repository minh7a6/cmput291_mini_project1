import sqlite3
import sys
from PostQuestions import Post
from SearchPost import SearchMain
def menu(uid,c):
    option = input("Select an option 1. Post a question 2.Search for post")
    if option =="1" :
        Post(uid,c)
    elif option =="2":
        SearchMain(c)
    