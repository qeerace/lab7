import sqlite3 as sqlite

def login(username,password):
    while True:
        with sqlite.connect("Quiz.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(username),(password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print ("Welcome "+username)
            return 1
        else:
            print ("Error, Try again")
            return 0
        break
login('user1','pass1')
