import sqlite3
from datetime import date
def SearchMain(c):
    print("\r\n------------------------------------------------Search Page------------------------------------------------")
    end = False
    while end ==False:
        keyword = input("Please input keyword(s) to search (please leave a space between each keyword)")
        keywordList = keyword.split()
        query = ""
        start =True
        for word in keywordList:
            if start == True:
                query = "SELECT * FROM posts p1 WHERE p1.title like '%"+word+"%' or p1.body like '%"+word+"%' UNION Select p1.pid, p1.pdate, p1.title, p1.body, p1.poster from posts p1, tags t1 WHERE p1.pid= t1.pid AND t1.tag like '%"+word+"%' "
                start = False
            else:
                query = query +"UNION SELECT * FROM posts p1 WHERE p1.title like '%"+word+"%' or p1.body like '%"+word+"%' UNION Select p1.pid, p1.pdate, p1.title, p1.body, p1.poster from posts p1, tags t1 WHERE p1.pid= t1.pid AND t1.tag like '%"+word+"%' "
        query = """With answerCount as (With countAnswer as (Select p1.title as title, count(a1.pid) as countAns, p1.pid as pid
                    From questions q1, posts p1, answers a1
                    WHERE p1.pid = q1.pid
                    AND q1.pid = a1.qid
                    group by q1.pid),
                    questionsTitle as(select posts.title as title, posts.pid as pid
                                      from posts, questions
                                      where posts.pid = questions.pid
                                      )
                    Select questionsTitle.title as title , COALESCE(countAnswer.countAns,0) as NumberOfAnswers, questionsTitle.pid
                    from questionsTitle
                    left join countAnswer
                    on countAnswer.pid = questionsTitle.pid),
                    
                    
                    CountVote as (SELECT p1.title , count (v1.pid) as countVotes, p1.pid as pid
                    From votes v1, posts p1
                    WHERE v1.pid = p1.pid
                    GROUP by p1.pid),
                    
                    keyword as ( """ + query + """ )
                    SELECT keyword.pid, keyword.pdate, keyword.title, keyword.body, keyword.poster, CountVote.countVotes as numberVotes, answerCount.NumberOfAnswers as NumberOfAnswers
                    FRom keyword
                    LEFT JOIN CountVote
                    on CountVote.pid = keyword.pid
                    LEFT join answerCount
                    on answerCount.pid =  keyword.pid"""
        c.execute(query)
        print(c.fetchall())
        returnPage = input("Would you like to return to the main menue? 1.Yes 2.No")
        if returnPage == "1":
            end =True




