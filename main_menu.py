import sqlite3
import sys
from PostQuestions import Post
def menu(uid,c):
    option = input("Select an option 1. Post a question 2.Search for post")
    if option =="1" :
        Post(uid,c)
    