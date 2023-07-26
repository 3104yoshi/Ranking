import sqlite3

class userCredentialAccessor:
    def getUser(userCredential):
        with sqlite3.connect('app.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM User WHERE UserName=? and PassWord=? ', (userCredential.userName, userCredential.password))
            return cursor.fetchall()
    
    def addUser(userCredential):
        with sqlite3.connect('app.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO User VALUES(?, ?, ?)', (userCredential.userName, userCredential.password, userCredential.updateDate))
    
    def checkUserIs(userCredential):
        with sqlite3.connect('app.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM User WHERE UserName=? ', (userCredential.userName, ))
            return cursor.fetchall()
