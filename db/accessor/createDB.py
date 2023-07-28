import sqlite3

dbname = 'app.db'
conn = sqlite3.connect(dbname)

# SQLiteを操作するためのカーソルを作成
cur = conn.cursor()

# テーブルの作成
cur.execute(
    'CREATE TABLE User(UserName TEXT PRIMARY KEY, PassWord TEXT, UpdateDate TEXT)'
)

conn.close()